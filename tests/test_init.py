import pytest
from rdict import Rdict


@pytest.mark.parametrize(("dict_"), [("a"), (12), (12.34)])
def test_copy_success(dict_):
    with pytest.raises(ValueError):
        Rdict(dict_)
