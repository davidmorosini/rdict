from typing import Type
import pytest
from rdict import Rdict


@pytest.mark.parametrize(
    ("dict_", "error"),
    [("a", ValueError), (12, TypeError), (12.34, TypeError), (None, TypeError)],
)
def test_raise_error(dict_, error):
    with pytest.raises(error):
        Rdict(dict_)
