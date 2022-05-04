import json

from l33t_w0rm import factory, loader
from l33t_w0rm.exploiter_types.brute_forcer import BruteForcer
from l33t_w0rm.exploiter_types.phisher import Phisher
from l33t_w0rm.exploiter_types.web_exploiter import WebExploiter


def main() -> None:
    factory.register("phisher", Phisher)
    factory.register("web_exploiter", WebExploiter)
    factory.register("brute_forcer", BruteForcer)

    with open('./plugin_system/plug_def.json') as file:
        data = json.load(file)
        loader.load_plugins(data["plugins"])
        exploiters = [factory.create(item) for item in data["exploiters"]]

    for exploiter in exploiters:
        exploiter.exploit()


if __name__ == "__main__":
    main()
