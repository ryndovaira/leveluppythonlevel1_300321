import pytest

from topic_05_data_structure.practice.dict_2_get_name_by_number import get_name_by_number

params = [
    ({}, "", "Dictionary is empty!"),
    ({"ira": ["1-2-3"]}, "", "Phone number is empty!"),

    ([], "", "Dictionary must be dict!"),
    ("dict", "", "Dictionary must be dict!"),

    ({"ira": ["1-2-3"]}, [], "Phone number must be str!"),
    ({"ira": ["1-2-3"]}, None, "Phone number must be str!"),

    ({"ira": ["1-2-3"]}, "3-3-3", "Can't find phone: 3-3-3"),
    ({"ira": ["1-2-3"]}, "1-2-3", ["ira"]),

    ({
         "ira": ["1-2-3"], 
         "ivan": ["7-7-7", "0-0-0"],
         "kate": ["7-7-7", "9-6-3-0", "0-0-0"],
         "oleg": ["7-7-7"]
     },
     "9-6-3-0",
     ["kate"]),

    ({
         "ira": ["1-2-3"], 
         "ivan": ["7-7-7", "0-0-0"],
         "kate": ["7-7-7", "9-6-3-0", "0-0-0"],
         "oleg": ["7-7-7"]
     },
     "0-0-0",
     ["ivan", "kate"]),

    ({
         "ira": ["1-2-3"], 
         "ivan": ["7-7-7", "0-0-0"],
         "kate": ["7-7-7", "9-6-3-0", "0-0-0"],
         "oleg": ["7-7-7"]
     },
     "7-7-7",
     ["ivan", "kate", "oleg"]),
]

ids = ["dict: %s | phone: %s => %s" % (my_dict, val, expected) for (my_dict, val, expected) in params]


@pytest.mark.parametrize(argnames="my_dict, phone, expected",
                         argvalues=params,
                         ids=ids)
def test_get_name_by_number(my_dict, phone, expected):
    assert get_name_by_number(my_dict, phone) == expected


