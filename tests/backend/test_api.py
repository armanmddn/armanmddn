from collections.abc import Mapping

from fastapi.testclient import TestClient

from packages.shared_platform.health import Probe
from packages.shared_platform.settings import AppSettings
from services.api.main import create_app


class FakeProbes:
    def __init__(self, healthy: bool) -> None:
        async def probe() -> None:
            if not healthy:
                raise ConnectionError("not available")

        self._checks = {"database": probe, "redis": probe}
        self.closed = False

    @property
    def checks(self) -> Mapping[str, Probe]:
        return self._checks

    @property
    def timeout_seconds(self) -> float:
        return 0.1

    async def close(self) -> None:
        self.closed = True


def test_liveness_does_not_depend_on_external_services() -> None:
    probes = FakeProbes(healthy=False)
    with TestClient(create_app(AppSettings(_env_file=None), probes)) as client:
        response = client.get("/health/live")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    assert probes.closed is True


def test_readiness_returns_503_when_dependencies_are_unavailable() -> None:
    with TestClient(create_app(AppSettings(_env_file=None), FakeProbes(False))) as client:
        response = client.get("/health/ready")

    assert response.status_code == 503
    assert response.json() == {
        "status": "unavailable",
        "checks": {"database": "unavailable", "redis": "unavailable"},
    }


def test_readiness_returns_200_when_dependencies_are_available() -> None:
    with TestClient(create_app(AppSettings(_env_file=None), FakeProbes(True))) as client:
        response = client.get("/health/ready")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_local_mini_app_origin_is_allowed() -> None:
    with TestClient(create_app(AppSettings(_env_file=None), FakeProbes(True))) as client:
        response = client.options(
            "/health/ready",
            headers={
                "Origin": "http://localhost:5173",
                "Access-Control-Request-Method": "GET",
            },
        )

    assert response.status_code == 200
    assert response.headers["access-control-allow-origin"] == "http://localhost:5173"
