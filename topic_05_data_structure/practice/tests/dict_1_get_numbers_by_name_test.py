import pytest

from topic_05_data_structure.practice.dict_1_get_numbers_by_name import get_numbers_by_name

params = [
    ({}, "", "Dictionary is empty!"),
    ({"ira": ["1-2-3"]}, "", "Name is empty!"),

    ([], "", "Dictionary must be dict!"),
    ("dict", "", "Dictionary must be dict!"),

    ({"ira": ["1-2-3"]}, [], "Name must be str!"),
    ({"ira": ["1-2-3"]}, None, "Name must be str!"),

    ({"ira": ["1-2-3"]}, "ivan", "Can't find name: ivan"),
    ({"ira": ["1-2-3"]}, "ira", ["1-2-3"]),
    ({"ira": ["1-2-3"],
      "ivan": ["33-44-55", "99-3-1"]},
     "ivan", ["33-44-55", "99-3-1"]),
]

ids = [f"dict: {my_dict} | word: {val} => {expected}" for (my_dict, val, expected) in params]


@pytest.mark.parametrize(argnames="my_dict, word, expected",
                         argvalues=params,
                         ids=ids)
def test_get_numbers_by_name(my_dict, word, expected):
    assert get_numbers_by_name(my_dict, word) == expected


