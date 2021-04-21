import pytest
from recursive_dict import Dict
from tests.mocks.dicts import example_dict


@pytest.mark.parametrize(
    (
        "dict_",
        "value",
        "value_type",
        "response"
    ),
    [
        (
            example_dict,
            None,
            "value",
            True
        ),
        (
            example_dict,
            "false_",
            "key",
            True
        ),
        (
            example_dict,
            [1, 4],
            "any",
            True
        ),
        (
            example_dict,
            "rapadura",
            "any",
            False
        )
    ]
)
def test_contains_success(
    dict_,
    value,
    value_type,
    response
):
    rdict = Dict(dict_)
    assert response == rdict.contains(value, value_type=value_type)


@pytest.mark.parametrize(
    (
        "dict_",
        "value",
        "value_type"
    ),
    [
        (
            {},
            None,
            "test"
        ),
        (
            {"a": 67},
            67,
            "a/b/teste/error/teste"
        ),
        (
            {"a": 67},
            67,
            None
        )
    ]
)
def test_contains_error(
    dict_,
    value,
    value_type
):
    rdict = Dict(dict_)
    with pytest.raises(KeyError):
        rdict.contains(value, value_type=value_type)
