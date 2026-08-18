from services.worker.main import HEARTBEAT_KEY, heartbeat, worker_cycle


class FakeRedis:
    def __init__(self) -> None:
        self.calls: list[tuple[str, str, int]] = []

    async def set(self, key: str, value: str, ex: int) -> None:
        self.calls.append((key, value, ex))


async def test_worker_heartbeat_expires_if_worker_stalls() -> None:
    redis = FakeRedis()

    await heartbeat(redis, ttl_seconds=60)  # type: ignore[arg-type]

    assert redis.calls == [(HEARTBEAT_KEY, "alive", 60)]


async def test_worker_does_not_heartbeat_when_a_dependency_is_down() -> None:
    async def healthy() -> None:
        return None

    async def unavailable() -> None:
        raise ConnectionError("database DSN must not leak")

    redis = FakeRedis()
    result = await worker_cycle(
        {"database": unavailable, "redis": healthy},
        timeout_seconds=0.1,
        redis=redis,  # type: ignore[arg-type]
        ttl_seconds=60,
    )

    assert result is False
    assert redis.calls == []
