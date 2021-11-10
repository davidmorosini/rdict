import pytest
from rdict import Rdict
from tests.mocks.dicts import example_dict


@pytest.mark.parametrize(
    (
        "dict_",
        "path",
        "default",
        "response"
    ),
    [
        (
            {"a": 1},
            "a",
            None,
            1
        ),
        (
            {"a": 1},
            "c",
            "exemplo",
            "exemplo"
        ),
        (
            example_dict,
            "a/a/1",
            None,
            3
        ),
        (
            example_dict,
            "a/a/4",
            None,
            None
        ),
        (
            example_dict,
            "a/a/",
            None,
            [1, 3, 4, {"nullable": None, "nullable_2": None}]
        ),
        (
            example_dict,
            "a/b/g",
            1,
            4
        ),
        (
            example_dict,
            "a/b/x/y/z/0/w",
            "default",
            7
        ),
        (
            example_dict,
            "a/b/x/y/z//////",
            "default",
            [
                {
                    "w": 7,
                    "foo": "bar"
                },
                {
                    "w": 9,
                    "field": False
                },
                {
                    "w": 9.87,
                    "g": [1, 4],
                    "field": [1, 4],
                    "3": [1, 4]
                }
            ]
        ),
        (
            example_dict,
            "//////",
            None,
            example_dict
        ),
        (
            example_dict,
            "",
            None,
            example_dict
        ),
        (
            example_dict,
            None,
            None,
            example_dict
        ),
        (
            example_dict,
            "////c///////",
            None,
            4
        ),
        (
            example_dict,
            "'1'",
            None,
            "fake integer"
        ),
        (
            example_dict,
            "a/b/x/y/z/2/'3'/0",
            None,
            1
        ),
        (
            example_dict,
            "a/b/x/y/z/2/'3'/4",
            "default",
            "default"
        ),
        (
            example_dict,
            "a/b/j/1/0",
            None,
            {}
        )
    ]
)
def test_get_success(
    dict_,
    path,
    default,
    response
):
    rdict = Rdict(dict_)
    resp = rdict.get(path, default)
    assert response == resp


@pytest.mark.parametrize(
    (
        "dict_",
        "path",
        "error_raise"
    ),
    [
        (
            example_dict,
            "a/a/1/s/k",
            TypeError
        ),
        (
            example_dict,
            "g/l",
            KeyError
        ),
        (
            example_dict,
            "a/b/teste/error/teste",
            KeyError
        ),
        (
            example_dict,
            "a/a/9",
            IndexError
        ),

    ]
)
def test_get_error(
    dict_,
    path,
    error_raise
):
    rdict = Rdict(dict_)
    with pytest.raises(error_raise):
        rdict.get(path, raise_error=True)
