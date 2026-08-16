"""Finance bot entry point with explicit fake and live adapters."""

import asyncio
import logging
from typing import Protocol

from packages.shared_platform.settings import AppSettings, get_settings

LOGGER = logging.getLogger(__name__)


class BotAdapter(Protocol):
    async def run(self) -> None: ...


class FakeBotAdapter:
    """No-network adapter for local startup and automated tests."""

    async def run(self) -> None:
        LOGGER.info("finance bot fake adapter is ready")
        await asyncio.Event().wait()

    async def run_once(self) -> None:
        """Validate fake-adapter startup without making a test wait forever."""

        LOGGER.info("finance bot fake adapter is ready")


class LiveBotAdapter:
    def __init__(self, token: str) -> None:
        self._token = token

    async def run(self) -> None:
        from aiogram import Bot, Dispatcher

        bot = Bot(token=self._token)
        dispatcher = Dispatcher()
        try:
            await dispatcher.start_polling(bot)
        finally:
            await bot.session.close()


def build_adapter(settings: AppSettings) -> BotAdapter:
    if settings.telegram_adapter == "fake":
        return FakeBotAdapter()
    assert settings.telegram_bot_token is not None  # validated by AppSettings
    return LiveBotAdapter(settings.telegram_bot_token.get_secret_value())


async def run(settings: AppSettings | None = None) -> None:
    await build_adapter(settings or get_settings()).run()


if __name__ == "__main__":
    asyncio.run(run())
