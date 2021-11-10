import pytest
from rdict import Rdict


@pytest.mark.parametrize(
    ("dict_", "paths", "response"),
    [
        (
            {"a": 4, "b": {"c": 5}},
            ["b/c"],
            {"a": 4, "b": {}},
        ),
        (
            {"a": 4, "b": {"c": 5}},
            ["b"],
            {"a": 4},
        ),
        (
            {"a": 4, "b": {"c": {"d": 5}}},
            ["a", "b/c/d"],
            {"b": {"c": {}}},
        ),
        (
            {"a": 4, "b": {"c": {"d": 5}}},
            ["a", "b/c/d", "b/c"],
            {"b": {}},
        ),
        (
            {"a": 4, "b": {"c": {"d": 5}}},
            ["a", "b/c/d", "b/c", "b"],
            {},
        ),
    ],
)
def test_delete_success(dict_, paths, response):
    rdict = Rdict(dict_)
    resp = rdict.delete(paths)
    assert response == resp


@pytest.mark.parametrize(
    ("dict_", "paths", "error_raise"),
    [
        (
            {"a": 4, "b": {"c": 5}},
            ["c"],
            KeyError,
        ),
        (
            {"a": 4, "b": {"c": {"d": 5}}},
            ["b/c", "b/c/d"],
            KeyError,
        ),
        (
            {"a": 4, "b": {"c": 5}},
            ["a/f"],
            TypeError,
        ),
        (
            {"a": 4, "b": [{"x": 90}]},
            ["b/56"],
            IndexError,
        ),
        (
            {"a": [90], "b": [{"d": 5}]},
            ["a/5", "b/3/d"],
            IndexError,
        ),
    ],
)
def test_delete_error(dict_, paths, error_raise):
    rdict = Rdict(dict_)
    with pytest.raises(error_raise):
        rdict.delete(paths)
    assert rdict.copy() == dict_
