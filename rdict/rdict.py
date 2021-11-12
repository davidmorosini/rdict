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


class Rdict(dict):
    def __init__(self, dict_: dict, sep: str = "/", use_copy: bool = True):
        dict_for_use = deepcopy(dict_) if use_copy else dict_
        super().__init__(dict_for_use)
        self._sep = sep
        self._use_copy = use_copy

    def copy(self) -> dict:
        return deepcopy(self)

    def get(self, path: str, default: Any = None, raise_error: bool = False) -> Any:
        indexes = path_to_array_keys(path)
        dict_copy = self.copy()
        return dict_recursive_get(indexes, dict_copy, default, raise_error)

    def set(self, path: str, value: Any) -> dict:
        indexes = path_to_array_keys(path)
        self = dict_recursive_set(indexes, self, value)
        return self.copy()

    def search(self, value: Any, is_key: bool, base_path: str = "") -> List[str]:
        recursion_classes = [type(self), dict, list]
        struct_base = self.get(base_path)
        return dict_recursive_search(value, struct_base, "", is_key, recursion_classes)

    def search_pair(self, key: Any, value: Any, base_path: str = "") -> List[str]:
        recursion_classes = [type(self), dict, list]
        struct_base = self.get(base_path)
        return dict_recursive_search_pair(
            key, value, struct_base, "", recursion_classes
        )

    def contains(
        self, value: Any, value_type: str = "any", base_path: str = ""
    ) -> bool:
        value_types = ["any", "key", "value"]
        if value_type not in value_types:
            raise KeyError(f"Param value_type '{value_type}' not in {value_types}")

        from_to = {
            "key": self.search(value, True, base_path=base_path),
            "value": self.search(value, False, base_path=base_path),
        }
        paths = from_to.get(value_type, list(from_to.values()))
        return any(paths)

    def contains_pair(self, key: Any, value: Any, base_path: str = "") -> bool:
        paths = self.search_pair(key, value, base_path=base_path)
        return any(paths)

    def delete(self, path: str) -> dict:
        indexes = path_to_array_keys(path)
        self = dict_recursive_del(indexes, self)
        return self.copy()
