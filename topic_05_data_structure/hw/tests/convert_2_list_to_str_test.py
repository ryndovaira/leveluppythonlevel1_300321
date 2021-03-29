import pytest

from topic_05_data_structure.hw.convert_2_list_to_str import list_to_str

params = [
    ([1, '2', 'awe', [1, 2, 3]], '!', ('1!2!awe![1, 2, 3]', 9)),

    ([1, 2, 3, 4], '!', ('1!2!3!4', 9)),
    ([1, 2, 3], ' ', ('1 2 3', 4)),
    ([1, 2, 3], ':', ('1:2:3', 4)),
    ([1, 2], '#', ('1#2', 1)),
    ([1], '#', ('1', 0)),

    ([], ' ', ()),

    (None, '', 'First arg must be list!'),
    (0, '', 'First arg must be list!'),
    ({}, '', 'First arg must be list!'),
    ((), '', 'First arg must be list!'),

    ([1, 2], None, 'Second arg must be str!'),
    ([1, 2], 0, 'Second arg must be str!'),
    ([1, 2], [], 'Second arg must be str!'),
    ([1, 2], 4.55, 'Second arg must be str!'),
]

ids = ["list: %s | sep: %s => %s" % (my_list, val, expected) for (my_list, val, expected) in params]


@pytest.mark.parametrize(argnames="my_list, sep, expected",
                         argvalues=params,
                         ids=ids)
def test_list_to_str(my_list, sep, expected):
    assert list_to_str(my_list, sep) == expected



