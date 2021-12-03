import pytest
from rdict.utils import (
    array_keys_to_path,
    key_to_path,
    path_to_key,
    path_to_array_keys,
    recognize_key,
)


@pytest.mark.parametrize(
    ("keys", "separator", "response"),
    [(["a", 5, "6"], "/", "a/5/'6'"), ([], "/", "")],
)
def test_array_keys_to_path(keys, separator, response):
    assert response == array_keys_to_path(keys, separator)


@pytest.mark.parametrize(
    ("key", "response"),
    [("test", "test"), ("5", "'5'"), (5, "5")],
)
def test_key_to_path(key, response):
    assert response == key_to_path(key)


@pytest.mark.parametrize(
    ("path", "response"),
    [("test", "test"), ("'5'", "5"), ("5", 5)],
)
def test_path_to_key(path, response):
    assert response == path_to_key(path)


@pytest.mark.parametrize(
    ("path", "separator", "response"),
    [("a/5/'6'", "/", ["a", 5, "6"]), ("", "/", [])],
)
def test_path_to_array_keys(path, separator, response):
    assert response == path_to_array_keys(path, separator)


@pytest.mark.parametrize(
    ("key", "origin_struct", "response"),
    [("test", True, "test"), (0, True, 0), (0, ["test"], 0)],
)
def test_recognize_key(key, origin_struct, response):
    assert response == recognize_key(key, origin_struct)
