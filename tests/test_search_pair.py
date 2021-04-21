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
            "as-9",
            2,
            ["/as-9"]
        ),
        (
            example_dict,
            "j",
            [{"t": None, "w": None}, [{}, {"w": "test"}, {"w": 90}]],
            ["/a/b/j"]
        ),
        (
            example_dict,
            "j",
            [{"t": 90, "w": None}, [{}, {"w": "test"}, {"w": None}]],
            []
        ),
        (
            example_dict,
            "w",
            None,
            ["/a/b/j/0/w"]
        ),
        (
            example_dict,
            "full",
            example_dict,
            []
        ),
        (
            {"a": {"7": 9.876554}},
            "7",
            9.876554,
            ["/a/'7'"]
        ),
        (
            {"a": [{"7": 9.876554}]},
            "7",
            9.876554,
            ["/a/0/'7'"]
        )
    ]
)
def test_search_pair_success(
    dict_,
    key,
    value,
    response
):
    rdict = Dict(dict_)
    paths = rdict.search_pair(key, value)
    assert sorted(response) == sorted(paths)
