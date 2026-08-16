"""Minimal worker lifecycle with a Redis heartbeat."""

import asyncio
import logging
from collections.abc import Mapping

from redis.asyncio import Redis

from packages.shared_platform.health import DependencyProbes, Probe, check_readiness
from packages.shared_platform.settings import AppSettings, get_settings

LOGGER = logging.getLogger(__name__)
HEARTBEAT_KEY = "platform:worker:heartbeat"


async def heartbeat(redis: Redis, ttl_seconds: int) -> None:
    """Publish an expiring marker so operations can detect a stalled worker."""

    await redis.set(HEARTBEAT_KEY, "alive", ex=ttl_seconds)


async def worker_cycle(
    checks: Mapping[str, Probe], timeout_seconds: float, redis: Redis, ttl_seconds: int
) -> bool:
    """Perform one dependency-gated unit of worker health behavior."""

    report = await check_readiness(checks, timeout_seconds)
    if not report.ready:
        LOGGER.error("worker dependencies unavailable: %s", report.checks)
        return False
    await heartbeat(redis, ttl_seconds)
    return True


async def run_once(settings: AppSettings | None = None) -> bool:
    """Check dependencies and publish one heartbeat; useful for health checks."""

    active_settings = settings or get_settings()
    probes = DependencyProbes(
        active_settings.database_url,
        active_settings.redis_url,
        active_settings.readiness_timeout_seconds,
    )
    redis = Redis.from_url(active_settings.redis_url)
    try:
        return await worker_cycle(
            probes.checks,
            probes.timeout_seconds,
            redis,
            active_settings.worker_heartbeat_ttl_seconds,
        )
    finally:
        await redis.aclose()
        await probes.close()


async def run(settings: AppSettings | None = None) -> None:
    """Keep the worker alive and refresh its observable heartbeat."""

    active_settings = settings or get_settings()
    interval = max(1, active_settings.worker_heartbeat_ttl_seconds // 2)
    while True:
        if not await run_once(active_settings):
            raise RuntimeError("worker dependencies are unavailable")
        await asyncio.sleep(interval)


def main() -> None:
    asyncio.run(run())


if __name__ == "__main__":
    main()
