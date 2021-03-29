import pytest

from topic_05_data_structure.hw.set_1_get_info_for_3_set import get_info_for_3_set

params = [
    (None, None, None, 'Must be set!'),
    ({1}, None, None, 'Must be set!'),
    (None, {1}, None, 'Must be set!'),
    (None, None, {1}, 'Must be set!'),

    ({1}, {1}, {1}, {'left == mid == right': True,
                     'left == mid': True,
                     'left == right': True,
                     'mid == right': True,
                     'left & mid': {1},
                     'left & right': {1},
                     'mid & right': {1},
                     'left <= mid': True,
                     'mid <= left': True,
                     'left <= right': True,
                     'right <= left': True,
                     'mid <= right': True,
                     'right <= mid': True}),

    ({1}, {2}, {3}, {'left == mid == right': False,
                     'left == mid': False,
                     'left == right': False,
                     'mid == right': False,
                     'left & mid': set(),
                     'left & right': set(),
                     'mid & right': set(),
                     'left <= mid': False,
                     'mid <= left': False,
                     'left <= right': False,
                     'right <= left': False,
                     'mid <= right': False,
                     'right <= mid': False}),

    ({1, 2, 3}, {1, 2}, {1, 3}, {'left == mid == right': False,
                                 'left == mid': False,
                                 'left == right': False,
                                 'mid == right': False,
                                 'left & mid': {1, 2},
                                 'left & right': {1, 3},
                                 'mid & right': {1},
                                 'left <= mid': False,
                                 'mid <= left': True,
                                 'left <= right': False,
                                 'right <= left': True,
                                 'mid <= right': False,
                                 'right <= mid': False}),
]


ids = ["left: %s | mid: %s | right: %s => %s" % (left, mid, right, expected) for (left, mid, right, expected) in params]


@pytest.mark.parametrize(argnames="left, mid, right, expected",
                         argvalues=params,
                         ids=ids)
def test_get_info_for_3_set(left, mid, right, expected):
    result = get_info_for_3_set(left, mid, right)
    assert result == expected
