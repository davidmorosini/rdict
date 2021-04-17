import pytest
from recursive_dict import Dict


@pytest.mark.parametrize(
    ("dict_"),
    [
        ("a"),
        (12),
        (12.34)
    ]
)
def test_copy_success(dict_):
    with pytest.raises(ValueError):
        Dict(dict_)
