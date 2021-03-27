import pytest

from topic_5_data_structure.practice.convert_2_dict_to_list import dict_to_list

params = [
    ([], 'Must be dict!'),
    ((), 'Must be dict!'),
    (None, 'Must be dict!'),
    ('ololo', 'Must be dict!'),
    (123, 'Must be dict!'),

    ({}, [[], [], 0, 0, False]),
    ({1: 'q'}, [[1], ['q'], 1, 1, False]),
    ({1: 'q', 2: 'w', 3: 3}, [[1, 2, 3], ['q', 'w', 3], 27, 3, True]),
    ({1: 'e', 2: 'w', 3: 'w'}, [[1, 2, 3], ['e', 'w', 'w'], 27, 2, False]),
    ({1: 'w', 2: 'w', 3: 'w'}, [[1, 2, 3], ['w', 'w', 'w'], 27, 1, False]),
]

ids = ["dict: %s => %s" % (my_dict, expected) for (my_dict, expected) in params]


@pytest.mark.parametrize(argnames="my_dict, expected",
                         argvalues=params,
                         ids=ids)
def test_dict_to_list(my_dict, expected):
    assert dict_to_list(my_dict) == expected



