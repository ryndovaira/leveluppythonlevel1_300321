import pytest

from topic_05_data_structure.hw.list_3_magic_reversal import magic_reversal

params = [
    ([], 'Empty list!'),

    (None, 'Must be list!'),
    ({}, 'Must be list!'),
    (1, 'Must be list!'),
    ((), 'Must be list!'),

    ([1], [1, 1, 1]),
    ([1,  'aa', 99], ['aa', 'aa', 99, 'aa', 1]),
    ([1, 'w'], [1, 'w', 'w', 1]),
]

ids = ["list: %s => %s" % (my_list, expected) for (my_list, expected) in params]


@pytest.mark.parametrize(argnames="my_list, expected",
                         argvalues=params,
                         ids=ids)
def test_magic_reversal(my_list, expected):
    if type(expected) != str:
        my_list_old = my_list.copy()

    assert magic_reversal(my_list) == expected

    if type(expected) != str:
        assert my_list_old == my_list



