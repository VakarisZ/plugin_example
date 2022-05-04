import importlib
from typing import List


class PluginInterface:

    @staticmethod
    def initialize():
        pass


def import_module(name: str) -> PluginInterface:
    return importlib.import_module(name)


def load_plugins(plugins: List[str]) -> None:
    for plugin_path in plugins:
        plugin = import_module(plugin_path)
        plugin.initialize()
