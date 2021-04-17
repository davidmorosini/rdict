from copy import deepcopy


class Dict:
    def __init__(self, dict_):
        if type(dict_) not in [dict, list]:
            raise ValueError(f"Not dict: {dict_}")
        self._dict = deepcopy(dict_)

    def copy(self):
        """
            Returns a deepcopy from data structure
        """
        pass

    def get(self, path, default=None):
        """
            returns an value by path or default case
            not found indexes
        """
        pass

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
