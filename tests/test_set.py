import pytest
from rdict import Rdict


@pytest.mark.parametrize(
    ("dict_", "path", "value", "response"),
    [
        ({}, "foo", "bar", {"foo": "bar"}),
        ({}, "a/b/b/0/1", 1, {"a": {"b": {"b": [[1]]}}}),
        ({}, "a/'5'/5", 1, {"a": {"5": [1]}}),
        (
            {"a": [0, {"b": [8]}]},
            "a/1/b/1",
            7,
            {"a": [0, {"b": [8, 7]}]},
        ),
        (
            {"a": [0, {"b": [8]}]},
            "a/1/b/",
            7,
            {"a": [0, {"b": 7}]},
        ),
        (
            {"a": [0, {"b": [8]}]},
            "a/1/b/0/t/0",
            7,
            {"a": [0, {"b": [{"t": [7]}]}]},
        ),
    ],
)
def test_set_success(dict_, path, value, response):
    rdict = Rdict(dict_)
    resp = rdict.set(path, value)
    assert response == resp
