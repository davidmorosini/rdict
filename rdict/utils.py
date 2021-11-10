from typing import Any, Union, List

from rdict.macros import INDEX_SPECIAL_CHARACTER


def key_to_path(key: Union[int, str]) -> str:
    if isinstance(key, str) and key.isnumeric():
        return f"{INDEX_SPECIAL_CHARACTER}{key}{INDEX_SPECIAL_CHARACTER}"
    return str(key)


def path_to_key(path: str) -> Union[int, str]:
    if path.isnumeric():
        return int(path)
    else:
        return path.replace(INDEX_SPECIAL_CHARACTER, "")


def array_keys_to_path(keys: List[Union[int, str]], separator: str = "/") -> str:
    formated_keys = [key_to_path(v) for v in keys]
    path = f"{separator}".join(formated_keys)
    return path


def path_to_array_keys(path: str, separator: str = "/") -> List[Union[int, str]]:
    splited_keys = path.split(separator)
    array_keys = [path_to_key(v) for v in splited_keys if v]
    return array_keys


def recognize_key(key: Union[int, str], origin_struct: Any) -> Union[int, str]:
    key_struct_types = [list, bool]
    if type(origin_struct) in key_struct_types:
        return key

    str_key = str(key)
    if str_key.isnumeric():
        return f"{INDEX_SPECIAL_CHARACTER}{key}{INDEX_SPECIAL_CHARACTER}"
    return key
