import pytest
from pydantic import ValidationError

from packages.shared_platform.settings import AppSettings


def test_fake_bot_is_safe_default() -> None:
    settings = AppSettings(_env_file=None)

    assert settings.telegram_adapter == "fake"
    assert settings.telegram_bot_token is None


def test_live_bot_requires_token() -> None:
    with pytest.raises(ValidationError, match="TELEGRAM_BOT_TOKEN"):
        AppSettings(telegram_adapter="live", _env_file=None)
