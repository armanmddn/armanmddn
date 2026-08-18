"""Typed, environment-driven configuration shared by platform processes."""

from functools import lru_cache
from typing import Literal

from pydantic import AliasChoices, Field, SecretStr, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """Runtime settings.

    Safe local defaults intentionally select the fake Telegram adapter. Real
    credentials are supplied only through the process environment.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        populate_by_name=True,
    )

    app_env: Literal["development", "test", "production"] = "development"
    app_log_level: str = "INFO"
    app_secret_key: SecretStr = SecretStr("local-development-only-change-me")
    database_url: str = "postgresql+asyncpg://platform:platform@postgres:5432/platform"
    redis_url: str = "redis://redis:6379/0"
    telegram_adapter: Literal["fake", "live"] = "fake"
    telegram_bot_token: SecretStr | None = Field(
        default=None,
        validation_alias=AliasChoices("TELEGRAM_BOT_TOKEN", "FINANCE_BOT_TOKEN"),
    )
    readiness_timeout_seconds: float = Field(default=2.0, gt=0)
    worker_heartbeat_ttl_seconds: int = Field(default=60, gt=1)
    cors_origins: list[str] = Field(default_factory=lambda: ["http://localhost:5173"])

    @model_validator(mode="after")
    def normalize_empty_token(self) -> "AppSettings":
        """Treat empty string token as None."""
        if self.telegram_bot_token is not None and self.telegram_bot_token.get_secret_value() == "":
            self.telegram_bot_token = None
        return self

    @model_validator(mode="after")
    def require_token_for_live_telegram(self) -> "AppSettings":
        if self.telegram_adapter == "live" and not (
            self.telegram_bot_token and self.telegram_bot_token.get_secret_value()
        ):
            raise ValueError("TELEGRAM_BOT_TOKEN is required for the live adapter")
        return self


@lru_cache
def get_settings() -> AppSettings:
    """Return one immutable-by-convention settings snapshot per process."""

    return AppSettings()
