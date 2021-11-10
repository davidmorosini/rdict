import pytest
from rdict import Rdict
from tests.mocks.dicts import example_dict


@pytest.mark.parametrize(
    (
        "dict_",
        "value",
        "is_key",
        "response"
    ),
    [
        (
            example_dict,
            None,
            False,
            [
                "/a/a/3/nullable",
                "/a/a/3/nullable_2",
                "/a/b/j/0/w",
                "/a/b/j/0/t",
            ]
        ),
        (
            example_dict,
            False,
            False,
            [
                "/false_",
                "/False",
                "/a/b/x/y/z/1/field"
            ]
        ),
        (
            example_dict,
            "w",
            True,
            [
                "/a/b/j/0/w",
                "/a/b/j/1/1/w",
                "/a/b/j/1/2/w",
                "/a/b/x/y/z/0/w",
                "/a/b/x/y/z/1/w",
                "/a/b/x/y/z/2/w"
            ]
        ),
        (
            example_dict,
            {},
            False,
            ["/a/b/j/1/0"]
        ),
        (
            example_dict,
            -56.67,
            False,
            ["/float_negative"]
        ),
        (
            example_dict,
            "key_not_found",
            True,
            []
        ),
        (
            example_dict,
            "value_not_found",
            False,
            []
        ),
        (
            example_dict,
            [1, 3, 4, {"nullable": None, "nullable_2": None}],
            False,
            ["/a/a"]
        ),
        (
            {"a": {"7": 9.876554}},
            "7",
            True,
            ["/a/'7'"]
        ),
        (
            {"a": [{"7": 9.876554}]},
            "7",
            True,
            ["/a/0/'7'"]
        ),
        (
            {"a": [{"7": [0, 1, 2, 3, 4, 5, 6, "7"]}]},
            "7",
            False,
            ["/a/0/'7'/7"]
        )
    ]
)
def test_search_success(
    dict_,
    value,
    is_key,
    response
):
    rdict = Rdict(dict_)
    none_paths = rdict.search(value, is_key)
    assert sorted(response) == sorted(none_paths)
