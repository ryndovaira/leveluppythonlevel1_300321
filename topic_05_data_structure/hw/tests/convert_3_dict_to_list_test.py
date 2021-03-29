import pytest

from topic_05_data_structure.hw.convert_3_dict_to_list import dict_to_list

params = [
    ([], 'Must be dict!'),
    ((), 'Must be dict!'),
    (None, 'Must be dict!'),
    ('ololo', 'Must be dict!'),
    (123, 'Must be dict!'),

    ({}, ([], [], 0, 0)),
    ({1: 'q'}, ([1], ['q'], 1, 1)),
    ({1: 'q', 2: 'w', 3: '3'}, ([1, 2, 3], ['q', 'w', '3'], 3, 3)),
    ({1: 'e', 2: 'w', 3: 'w'}, ([1, 2, 3], ['e', 'w', 'w'], 3, 2)),
    ({1: 'w', 2: 'w', 3: 'w'}, ([1, 2, 3], ['w', 'w', 'w'], 3, 1)),
]

ids = ["dict: %s => %s" % (my_dict, expected) for (my_dict, expected) in params]


@pytest.mark.parametrize(argnames="my_dict, expected",
                         argvalues=params,
                         ids=ids)
def test_dict_to_list(my_dict, expected):
    assert dict_to_list(my_dict) == expected



