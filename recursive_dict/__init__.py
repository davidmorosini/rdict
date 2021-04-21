from copy import deepcopy


class Dict:
    def __init__(self, dict_, sep="/", use_copy=True):
        if type(dict_) not in [dict, list]:
            raise ValueError(f"Not dict: {dict_}")
        self._dict = deepcopy(dict_) if use_copy else dict_
        self._sep = sep
        self._use_copy = use_copy

    def copy(self):
        """
            Returns a deepcopy from internal dict structure

            :return: deepcopy from internal dict
            :rtype: dict
        """
        return deepcopy(self._dict)

    def _recognize_key(self, key, struct_from):
        """
            Function to diferentiate a index number to string key number

            :param key: Value of key with recognize
            :type key: str
            :param struct_from: Data struct of value origins
            :type struct_from: object

            :return: dict key recognized
            :rtype: object
        """
        if any([
            isinstance(struct_from, list),
            isinstance(key, bool)
        ]):
            return key

        try:
            int(key)
            return f"'{key}'"
        except ValueError:
            return key

    def _split_path(self, path):
        """
            Split the string path into a list of keys that make up the full
            path

            :param path: Path from resource in dict
            :type path: str

            :note: To differentiate a numeric index (of a vector) from a
                numeric key as a string just add quotes in the key.
                Ex: "key/5/'123'/resource"

            :return: List of keys from path
            :rtype: list[str]
        """
        def __convert(value):
            """
                Converts each part of the path to a numeric or key index

                :param value: Part of path
                :type value: str
            """
            try:
                return int(value)
            except ValueError:
                return value.replace("'", "").replace("\"", "")
        return [__convert(p) for p in path.split(self._sep) if p]

    def _recursive_get(self, indexes, dict_, default, raise_):
        """
            Protected basis function for creating the key search recursion
            within the structure

            :param indexes: List of keys from path
            :type indexes: list
            :param dict_: Current dict structure in recursion
            :type dict_: object
            :param default: Default value to be returned in case of key not
                found
            :type default: object
            :param raise_: Flag to indicate an error when searching for the
                indicated path
            :type raise_error: bool

            :return: Value of path or default
            :rtype: object
        """
        current_len = len(indexes)
        current_index = indexes[0]
        try:
            current_resp = dict_[current_index]
        except (KeyError, TypeError, IndexError) as err:
            if not raise_:
                return default
            raise err

        if current_len == 1:
            return current_resp
        return self._recursive_get(indexes[1:], current_resp, default, raise_)

    def get(self, path, default=None, raise_error=False):
        """
            Returns the value according to the provided path or the default
            value if it does not exist

            :param path: Indicates a path to the resource
            :type path: str
            :param default: Default value to be returned in case of key not
                found
            :type default: object
            :param raise_error: Flag to indicate an error when searching for
                the indicated path
            :type raise_error: bool

            :return: Found value or default
            :rtype: object
        """
        indexes = path and self._split_path(path)
        if not indexes:
            return self.copy()
        return deepcopy(
            self._recursive_get(indexes, self._dict, default, raise_error)
        )

    def _recursive_set(self, indexes, dict_, value):
        """
            Protected basis function for creating the path indicates and
            populates with value inputed

            :param indexes: List of keys from path
            :type indexes: list
            :param dict_: Current dict structure in recursion
            :type dict_: object
            :param value: New value
            :type default: object

            :return: Current data structure in recursion
            :rtype: object
        """
        current_index = indexes[0]
        current_len = len(indexes)

        try:
            current_value = dict_[current_index]
        except IndexError:
            if current_len == 1:
                dict_.append(value)
                return dict_
            current_value = {} if isinstance(indexes[1], str) else []
            aux = self._recursive_set(indexes[1:], current_value, value)
            dict_.append(aux)
            return dict_
        except TypeError:
            if current_len == 1:
                str_instance = isinstance(current_index, str)
                aux = {current_index: value}
                current_value = aux if str_instance else [value]
                return current_value
            current_value = {} if isinstance(indexes[1], str) else []
            aux = self._recursive_set(indexes[1:], current_value, value)
            if isinstance(current_index, str):
                return {current_index: aux}
            return [aux]
        except KeyError:
            if current_len == 1:
                dict_[current_index] = value
                return dict_
            current_value = {} if isinstance(indexes[1], str) else []
            aux = self._recursive_set(indexes[1:], current_value, value)
            dict_[current_index] = aux
            return dict_

        if current_len == 1:
            dict_[current_index] = value
            return dict_

        dict_[current_index] = self._recursive_set(
            indexes[1:], current_value, value
        )
        return dict_

    def set(self, path, value):
        """
            Replace value in path or create the path and add value

            :param path: Indicates a path to the resource
            :type path: str
            :param value: New value to be insert
            :type value: object

            :return: deepcopy from current data structure
            :rtype: dict
        """
        indexes = self._split_path(path)
        self.dict_ = self._recursive_set(indexes, self._dict, value)
        return self.copy()

    def _recursive_search(self, value, dict_, current_path, is_key):
        """
            Protected basis function to be search an value (key/value)
            in data structure and return all paths to resource

            :param value: Value to be search in data structure
            :type value: object
            :param dict_: Current branch of data structure
            :type dict_: dict or list
            :param current_path: Current path
            :type current_path: str
            :param is_key: Flag to indicate if value is key or value
            :type is_key: bool

            :return: Current list of found paths
            :rtype: list
        """
        found = []
        if type(dict_) not in [dict, list]:
            return found

        it = dict_.items() if isinstance(dict_, dict) else enumerate(dict_)
        for key_, value_ in it:
            aux_path = self._recognize_key(key_, dict_)
            new_path = f"{current_path}/{aux_path}"

            if any([
                is_key and key_ == value,
                not is_key and value_ == value
            ]):
                found.append(new_path)

            deep_found = self._recursive_search(
                value, value_, new_path, is_key
            )
            found.extend(deep_found)
        return found

    def search(self, value, is_key):
        """
            Method to search an value or key in data structure and return
            all paths to resource

            :param value: Value to be search
            type value: object
            :param is_key: Flag to indicate if value is key or value
            :type is_key: bool

            :return: List of all paths found with resource
            :rtype: list
        """
        return self._recursive_search(value, self._dict, "", is_key)

    def _recursive_search_pair(self, key, value, dict_, current_path):
        """
            Protected basis function to be search an pair (key/value)
            in data structure and return all paths to resource

            :param key: Key to be search in data structure
            :type key: object
            :param value: Value to be search in data structure
            :type value: object
            :param dict_: Current branch of data structure
            :type dict_: dict or list
            :param current_path: Current path
            :type current_path: str

            :return: Current list of found paths
            :rtype: list
        """
        found = []
        if type(dict_) not in [dict, list]:
            return found

        it = dict_.items() if isinstance(dict_, dict) else enumerate(dict_)
        for key_, value_ in it:
            aux_path = self._recognize_key(key_, dict_)
            new_path = f"{current_path}/{aux_path}"

            if all([
                key_ == key,
                value_ == value
            ]):
                found.append(new_path)

            deep_found = self._recursive_search_pair(
                key, value, value_, new_path
            )
            found.extend(deep_found)

        return found

    def search_pair(self, key, value):
        """
            Method to search an pair (key/value) in data structure and return
            all paths to resource

            :param key: Key to be search in data structure
            :type key: object
            :param value: Value to be search in data structure
            type value: object

            :return: List of all paths found with resource
            :rtype: list
        """
        return self._recursive_search_pair(key, value, self._dict, "")

    def contains(self, value, value_type="any"):
        """
            Method to check if data structure contains value or key

            :param value: Value to be fetched
            type value: object
            :param value_type: Specifies the type of value to be fetched
            :type is_key: str

            :return: True or False
            :rtype: bool
        """
        value_types = ["any", "key", "value"]
        if value_type not in value_types:
            raise KeyError(
                f"Param value_type '{value_type}' not in {value_types}"
            )

        from_to = {
            "key": self.search(value, True),
            "value": self.search(value, False)
        }
        paths = from_to.get(value_type, [from_to["key"], from_to["value"]])
        return any(paths)

    def contains_pair(self, key, value):
        """
            Method to check if data structure contains pair key and value

            :param key: Key to be fetched
            :param value: Value to be fetched
            type value: object

            :return: True or False
            :rtype: bool
        """
        paths = self.search_pair(key, value)
        return any(paths)

    def delete(self, paths):
        """
            Delete same paths
        """
        pass
