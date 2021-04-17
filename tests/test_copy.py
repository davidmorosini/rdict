import pytest
from recursive_dict import Dict
from tests.mocks.dicts import example_dict


@pytest.mark.parametrize(
    (
        "dict_",
        "response"
    ),
    [
        (
            {"a": 1},
            {"a": 1}
        ),
        (
            {"a": {"b": 2, "c": [1, 2]}},
            {"a": {"b": 2, "c": [1, 2]}},
        ),
        (
            example_dict,
            example_dict
        )
    ]
)
def test_copy_success(
    dict_,
    response
):
    rdict = Dict(dict_)
    resp = rdict.copy()
    assert response == resp
