example_dict = {
    65: "integer",
    "1": "fake integer",
    3.14: "float",
    "3.14": "fake float",
    0.345: "float 2",
    ".345": "fake float 2",
    123.0: "float 3",
    "123.": " fake float 3",
    "false_": False,
    "true_": True,
    False: False,
    True: True,
    -3.0: "float negative",
    "-3.1": "fake float negative",
    "negative": -45,
    "float_negative": -56.67,
    "a": {
        "a": [1, 3, 4, {"nullable": None, "nullable_2": None}],
        "b": {
            "f": 3,
            "g": 4,
            "x": {
                "y": {
                    "z": [
                        {"w": 7, "foo": "bar"},
                        {"w": 9, "field": False},
                        {"w": 9.87, "g": [1, 4], "field": [1, 4], "3": [1, 4]},
                    ]
                }
            },
            "j": [{"t": None, "w": None}, [{}, {"w": "test"}, {"w": 90}]],
        },
    },
    "c": 4,
    "as-9": 2,
    "tt": {"aa": [1, 4]},
}
