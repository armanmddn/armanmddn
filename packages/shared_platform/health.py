"""Dependency probes used by API readiness and background processes."""

import asyncio
from collections.abc import Awaitable, Callable, Mapping
from dataclasses import dataclass
from typing import Protocol

from redis.asyncio import Redis
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

Probe = Callable[[], Awaitable[None]]


class ReadinessProvider(Protocol):
    @property
    def checks(self) -> Mapping[str, Probe]: ...

    @property
    def timeout_seconds(self) -> float: ...

    async def close(self) -> None: ...


@dataclass(frozen=True)
class ReadinessReport:
    ready: bool
    checks: Mapping[str, str]


class DependencyProbes:
    """Own lazy clients and expose bounded readiness checks."""

    def __init__(self, database_url: str, redis_url: str, timeout_seconds: float) -> None:
        self._engine: AsyncEngine = create_async_engine(database_url, pool_pre_ping=True)
        self._redis = Redis.from_url(redis_url)
        self._timeout = timeout_seconds

    async def database(self) -> None:
        async with self._engine.connect() as connection:
            await connection.execute(text("SELECT 1"))

    async def redis(self) -> None:
        if not await self._redis.ping():
            raise ConnectionError("Redis ping returned a false response")

    async def close(self) -> None:
        await self._engine.dispose()
        await self._redis.aclose()

    @property
    def checks(self) -> Mapping[str, Probe]:
        return {"database": self.database, "redis": self.redis}

    @property
    def timeout_seconds(self) -> float:
        return self._timeout


async def check_readiness(
    checks: Mapping[str, Probe], timeout_seconds: float
) -> ReadinessReport:
    """Run every check and report failures without leaking exception details."""

    async def run(name: str, probe: Probe) -> tuple[str, str]:
        try:
            await asyncio.wait_for(probe(), timeout=timeout_seconds)
        except Exception:  # readiness deliberately maps dependency failures to a status
            return name, "unavailable"
        return name, "ok"

    results = await asyncio.gather(*(run(name, probe) for name, probe in checks.items()))
    statuses = dict(results)
    return ReadinessReport(ready=all(value == "ok" for value in statuses.values()), checks=statuses)
