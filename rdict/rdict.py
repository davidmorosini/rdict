from typing import Any, List
from copy import deepcopy

from rdict.utils import path_to_array_keys
from rdict.recursive import (
    dict_recursive_get,
    dict_recursive_set,
    dict_recursive_search,
    dict_recursive_search_pair,
    dict_recursive_del,
)


class Rdict:
    def __init__(self, dict_: dict, sep: str = "/", use_copy: bool = True):
        if type(dict_) not in [dict, list]:
            raise ValueError(f"Not dict: {dict_}")
        self._dict = deepcopy(dict_) if use_copy else dict_
        self._sep = sep
        self._use_copy = use_copy

    def copy(self) -> dict:
        return deepcopy(self._dict)

    def get(self, path: str, default: Any = None, raise_error: bool = False) -> Any:
        indexes = path_to_array_keys(path)
        dict_copy = self.copy()
        return dict_recursive_get(indexes, dict_copy, default, raise_error)

    def set(self, path: str, value: Any) -> dict:
        indexes = path_to_array_keys(path)
        self._dict = dict_recursive_set(indexes, self._dict, value)
        return self.copy()

    def search(self, value: Any, is_key: bool) -> List[str]:
        return dict_recursive_search(value, self._dict, "", is_key)

    def search_pair(self, key: Any, value: Any) -> List[str]:
        return dict_recursive_search_pair(key, value, self._dict, "")

    def contains(self, value: Any, value_type: str = "any") -> bool:
        value_types = ["any", "key", "value"]
        if value_type not in value_types:
            raise KeyError(f"Param value_type '{value_type}' not in {value_types}")

        from_to = {"key": self.search(value, True), "value": self.search(value, False)}
        paths = from_to.get(value_type, list(from_to.values()))
        return any(paths)

    def contains_pair(self, key: Any, value: Any) -> bool:
        paths = self.search_pair(key, value)
        return any(paths)

    def delete(self, path: str) -> dict:
        indexes = path_to_array_keys(path)
        self._dict = dict_recursive_del(indexes, self._dict)
        return self.copy()
