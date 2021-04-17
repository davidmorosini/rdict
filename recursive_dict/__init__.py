from copy import deepcopy


class Dict:
    def __init__(self, dict_, sep="/"):
        if type(dict_) not in [dict, list]:
            raise ValueError(f"Not dict: {dict_}")
        self._dict = deepcopy(dict_)
        self._sep = sep

    def copy(self):
        """
            Returns a deepcopy from internal dict structure

            :return: deepcopy from internal dict
            :rtype: dict
        """
        return deepcopy(self._dict)

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
            :param raise_error: Flag to indicate an error when searching for the
                indicated path
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

    def set(self, path, value):
        """
            Set a new value in the path
        """
        pass

    def delete(self, paths):
        """
            Delete same paths
        """
        pass
