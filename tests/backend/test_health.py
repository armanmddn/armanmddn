import asyncio

from packages.shared_platform.health import check_readiness


async def test_readiness_reports_all_healthy_dependencies() -> None:
    async def healthy() -> None:
        return None

    report = await check_readiness({"database": healthy, "redis": healthy}, 0.1)

    assert report.ready is True
    assert report.checks == {"database": "ok", "redis": "ok"}


async def test_readiness_redacts_dependency_errors_and_timeouts() -> None:
    async def broken() -> None:
        raise RuntimeError("secret connection details")

    async def slow() -> None:
        await asyncio.sleep(0.05)

    report = await check_readiness({"database": broken, "redis": slow}, 0.001)

    assert report.ready is False
    assert report.checks == {"database": "unavailable", "redis": "unavailable"}
