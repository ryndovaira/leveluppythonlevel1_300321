import pytest

from topic_5_data_structure.hw.list_2_magic_mul import magic_mul

params = [
    ([], 'Empty list!'),

    (None, 'Must be list!'),
    ({}, 'Must be list!'),
    (1, 'Must be list!'),
    ((), 'Must be list!'),

    ([1], [1, 1, 1, 1, 1]),
    ([1, 'w'], [1, 1, 'w', 1, 'w', 1, 'w', 'w']),
]

ids = ["list: %s => %s" % (my_list, expected) for (my_list, expected) in params]


@pytest.mark.parametrize(argnames="my_list, expected",
                         argvalues=params,
                         ids=ids)
def test_magic_mul(my_list, expected):
    assert magic_mul(my_list) == expected



