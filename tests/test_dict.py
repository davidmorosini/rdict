import pytest
from recursive_dict import Dict


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
        )
    ]
)
def test_get_success_response(
    dict_,
    response
):
    rdict = Dict(dict_)
    resp = rdict.copy()
    assert response == resp
