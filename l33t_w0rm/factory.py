from typing import Callable, Dict, Any

from l33t_w0rm.exploiter import Exploiter

exploiter_creation_funcs: Dict[str, Callable[..., Exploiter]] = {}


def register(exploiter_type: str, creation_func: Callable[..., Exploiter]):
    """Register a new exploiter type"""
    exploiter_creation_funcs[exploiter_type] = creation_func


def unregister(exploiter_type: str):
    exploiter_creation_funcs.pop(exploiter_type, None)


def create(args: dict[str, Any]) -> Exploiter:
    args_copy = args.copy()
    exploiter_type = args_copy.pop("type")
    try:
        creation_func = exploiter_creation_funcs[exploiter_type]
        return creation_func(**args_copy)
    except KeyError:
        raise ValueError(f"Unknown exploiter type {exploiter_type!r}")
