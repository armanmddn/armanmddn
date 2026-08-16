import importlib.util
from pathlib import Path

from packages.shared_platform.settings import AppSettings


def load_bot_module():
    path = Path(__file__).parents[2] / "apps" / "finance-bot" / "main.py"
    spec = importlib.util.spec_from_file_location("finance_bot_main", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


async def test_fake_adapter_runs_without_token_or_network() -> None:
    module = load_bot_module()
    settings = AppSettings(_env_file=None)

    adapter = module.build_adapter(settings)
    await adapter.run_once()

    assert isinstance(adapter, module.FakeBotAdapter)
