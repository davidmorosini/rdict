from typing import Any, List, Union

from rdict.utils import recognize_key


def dict_recursive_get(
    indexes: List[Union[int, str]], dict_: dict, default: Any, raise_: bool
) -> Any:
    if not indexes:
        return dict_

    try:
        current_index = indexes[0]
        current_structure = dict_[current_index]
    except (KeyError, TypeError, IndexError) as err:
        if raise_:
            raise err
        return default

    if len(indexes) == 1:
        return current_structure

    next_path_indexes = indexes[1:]
    return dict_recursive_get(next_path_indexes, current_structure, default, raise_)


def dict_recursive_set(indexes: List[Union[int, str]], dict_: dict, value: Any) -> dict:
    current_index = indexes[0]
    current_len = len(indexes)

    try:
        current_value = dict_[current_index]
    except IndexError:
        if current_len == 1:
            dict_.append(value)
            return dict_
        current_value = {} if isinstance(indexes[1], str) else []
        aux = dict_recursive_set(indexes[1:], current_value, value)
        dict_.append(aux)
        return dict_
    except TypeError:
        if current_len == 1:
            str_instance = isinstance(current_index, str)
            aux = {current_index: value}
            current_value = aux if str_instance else [value]
            return current_value
        current_value = {} if isinstance(indexes[1], str) else []
        aux = dict_recursive_set(indexes[1:], current_value, value)
        if isinstance(current_index, str):
            return {current_index: aux}
        return [aux]
    except KeyError:
        if current_len == 1:
            dict_[current_index] = value
            return dict_
        current_value = {} if isinstance(indexes[1], str) else []
        aux = dict_recursive_set(indexes[1:], current_value, value)
        dict_[current_index] = aux
        return dict_

    if current_len == 1:
        dict_[current_index] = value
        return dict_

    dict_[current_index] = dict_recursive_set(indexes[1:], current_value, value)
    return dict_


def dict_recursive_search(
    value: Any,
    dict_: dict,
    current_path: str,
    is_key: bool,
    recursion_class_: List[Any],
) -> List[str]:

    found = []
    if type(dict_) not in recursion_class_:
        return found

    it = dict_.items() if isinstance(dict_, dict) else enumerate(dict_)
    for key_, value_ in it:
        aux_path = recognize_key(key_, dict_)
        new_path = f"{current_path}/{aux_path}"

        if any([is_key and key_ == value, not is_key and value_ == value]):
            found.append(new_path)

        deep_found = dict_recursive_search(
            value, value_, new_path, is_key, recursion_class_
        )
        found.extend(deep_found)
    return found


def dict_recursive_search_pair(
    key: Union[int, str],
    value: Any,
    dict_: dict,
    current_path: str,
    recursion_class_: List[Any],
) -> List[Any]:
    found = []
    if type(dict_) not in recursion_class_:
        return found

    it = dict_.items() if isinstance(dict_, dict) else enumerate(dict_)
    for key_, value_ in it:
        aux_path = recognize_key(key_, dict_)
        new_path = f"{current_path}/{aux_path}"

        if all([key_ == key, value_ == value]):
            found.append(new_path)

        deep_found = dict_recursive_search_pair(
            key, value, value_, new_path, recursion_class_
        )
        found.extend(deep_found)

    return found


def dict_recursive_del(indexes: List[Union[int, str]], dict_: dict) -> dict:
    current_index = indexes[0]
    current_len = len(indexes)

    if current_len == 2:
        last_index = indexes[-1]
        del dict_[current_index][last_index]
        return dict_
    elif current_len == 1:
        del dict_[current_index]
        return dict_

    next_indexes = indexes[1:]
    next_struct = dict_[current_index]
    dict_[current_index] = dict_recursive_del(next_indexes, next_struct)

    return dict_
