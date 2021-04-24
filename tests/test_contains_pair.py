import pytest
from recursive_dict import Dict
from tests.mocks.dicts import example_dict


@pytest.mark.parametrize(
    (
        "dict_",
        "key",
        "value",
        "response"
    ),
    [
        (
            example_dict,
            "field",
            False,
            True
        ),
        (
            example_dict,
            "field",
            True,
            False
        ),
        (
            example_dict,
            "t",
            None,
            True
        ),
        (
            example_dict,
            123.,
            "float 3",
            True
        ),
        (
            example_dict,
            "tt",
            {"aa": [1, 4]},
            True
        ),
        (
            example_dict,
            "j",
            [{"t": None, "w": None}, [{}, {"w": "test"}, {"w": 90}]],
            True
        ),
        (
            example_dict,
            "j",
            [{"t": 90, "w": None}, [{}, {"w": "test"}, {"w": None}]],
            False
        )
    ]
)
def test_contains_pair_success(
    dict_,
    key,
    value,
    response
):
    rdict = Dict(dict_)
    assert response == rdict.contains_pair(key, value)