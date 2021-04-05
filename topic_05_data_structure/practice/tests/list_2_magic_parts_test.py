import pytest

from topic_05_data_structure.practice.list_2_magic_parts import magic_parts

params = [
    ([], 'Empty list!'),

    (None, 'Must be list!'),
    ({}, 'Must be list!'),
    (1, 'Must be list!'),
    ((), 'Must be list!'),

    ([1], [1, 1, 1]),
    ([1, 'w'], [1, 'w', 'w', 2]),
    ([1, 'w', 777], [1, 'w', 777, 3]),
]

ids = ["list: %s => %s" % (my_list, expected) for (my_list, expected) in params]


@pytest.mark.parametrize(argnames="my_list, expected",
                         argvalues=params,
                         ids=ids)
def test_magic_parts(my_list, expected):
    assert magic_parts(my_list) == expected



