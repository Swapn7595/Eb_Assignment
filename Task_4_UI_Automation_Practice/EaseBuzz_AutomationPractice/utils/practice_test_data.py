import json
import os
from typing import Any, Dict, List, Optional

from utils.errors import TestDataError

_data_cache: Optional[Dict[str, List[str]]] = None


def practice_test_data_path() -> str:
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(root, "data", "test_data.json")


def _as_str_list(value: Any, field: str) -> List[str]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise TestDataError(f'"{field}" must be a JSON array, got {type(value).__name__}')
    out: List[str] = []
    for i, item in enumerate(value):
        if not isinstance(item, str):
            raise TestDataError(f'"{field}[{i}]" must be a string, got {type(item).__name__}')
        out.append(item)
    return out


def load_practice_test_data() -> dict:
    """Load and validate ``data/test_data.json``. Result is cached for the process."""
    global _data_cache
    if _data_cache is not None:
        return _data_cache

    path = practice_test_data_path()
    if not os.path.isfile(path):
        raise TestDataError(f"File not found: {path}")

    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise TestDataError(f"Invalid JSON in {path}: {e}") from e
    except OSError as e:
        raise TestDataError(f"Cannot read {path}: {e}") from e

    if not isinstance(data, dict):
        raise TestDataError("Root JSON value must be an object")

    radios = _as_str_list(data.get("radio_values"), "radio_values")
    drops = _as_str_list(data.get("dropdown_options"), "dropdown_options")

    _data_cache = {"radio_values": radios, "dropdown_options": drops}
    return _data_cache


def clear_practice_test_data_cache() -> None:
    """Clear cache (e.g. for tests that reload data)."""
    global _data_cache
    _data_cache = None
