import pytest

from topic_05_data_structure.practice.list_1_count_num import count_num

params = [
    (None, 0, 'First arg must be list!'),
    ([1], None, 'Second arg must be int!'),
    ([], 1, 'Empty list!\n'),
    (None, None, 'First arg must be list!\nSecond arg must be int!\n'),
    ([], None, 'Empty list!\nSecond arg must be int!\n'),

    ([1, 1, 1], 1, 3)
]

ids = ["list: %s | num: %s => %s" % (my_list, num, expected) for (my_list, num, expected) in params]


@pytest.mark.parametrize(argnames="my_list, num, expected",
                         argvalues=params,
                         ids=ids)
def test_count_num(my_list, num, expected):
    assert count_num(my_list, num) == expected
