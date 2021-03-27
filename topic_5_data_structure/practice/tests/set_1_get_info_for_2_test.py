import pytest

from topic_5_data_structure.practice.set_1_get_info_for_2 import get_info_for_2

params = [
    # left, right, expected
    ([], set(), 'Must be set!'),    # равно [[], set(), 'Must be set!']
    (set(), [], 'Must be set!'),
    ({1, 2, 3}, {1, 2, 3}, {
        'left == right': True,      # равенство
        'left & right': {1, 2, 3},  # intersection
        'left <= right': True,      # issubset
        'right <= left': True,      # issubset
    }),
    ({1, 2, 3}, {4, 5, 6}, {
        'left == right': False,     # равенство
        'left & right': set(),      # intersection
        'left <= right': False,     # issubset
        'right <= left': False,     # issubset
    }),
    ({1, 2, 3}, {3, 4, 5, 6}, {
        'left == right': False,     # равенство
        'left & right': {3},        # intersection
        'left <= right': False,     # issubset
        'right <= left': False,     # issubset
    }),
    (set(), {3, 4, 5, 6}, {
        'left == right': False,     # равенство
        'left & right': set(),      # intersection
        'left <= right': True,      # issubset
        'right <= left': False,     # issubset
    }),
]

ids = [f"left={left} | right={right} => {expected}" for (left, right, expected) in params]


@pytest.mark.parametrize(argnames="left, right, expected",
                         argvalues=params,
                         ids=ids)
def test(left, right, expected):
    assert get_info_for_2(left, right) == expected
