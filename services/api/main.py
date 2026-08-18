"""FastAPI application factory and process entry point."""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, Response, status
from fastapi.middleware.cors import CORSMiddleware

from packages.shared_platform.health import DependencyProbes, ReadinessProvider, check_readiness
from packages.shared_platform.settings import AppSettings, get_settings


def create_app(
    settings: AppSettings | None = None,
    probes: ReadinessProvider | None = None,
) -> FastAPI:
    configured_settings = settings or get_settings()
    configured_probes = probes or DependencyProbes(
        configured_settings.database_url,
        configured_settings.redis_url,
        configured_settings.readiness_timeout_seconds,
    )

    @asynccontextmanager
    async def lifespan(application: FastAPI) -> AsyncIterator[None]:
        application.state.probes = configured_probes
        yield
        await configured_probes.close()

    application = FastAPI(title="Telegram Product Platform API", lifespan=lifespan)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=configured_settings.cors_origins,
        allow_credentials=False,
        allow_methods=["GET"],
        allow_headers=["Accept"],
    )

    @application.get("/health/live", tags=["health"])
    async def live() -> dict[str, str]:
        return {"status": "ok"}

    @application.get("/health/ready", tags=["health"])
    async def ready(request: Request, response: Response) -> dict[str, object]:
        active_probes: ReadinessProvider = request.app.state.probes
        report = await check_readiness(active_probes.checks, active_probes.timeout_seconds)
        if not report.ready:
            response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {"status": "ok" if report.ready else "unavailable", "checks": report.checks}

    return application


app = create_app()
