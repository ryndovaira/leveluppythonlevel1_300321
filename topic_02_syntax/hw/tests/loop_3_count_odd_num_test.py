import pytest

from topic_02_syntax.hw.loop_3_count_odd_num import count_odd_num

params = [
    (1.23, "Must be int!"),
    (-1.34, "Must be int!"),
    ("5", "Must be int!"),
    (True, "Must be int!"),
    (-5, "Must be > 0!"),
    (0, "Must be > 0!"),
    (1, 1),
    (2, 0),
    (4, 0),
    (10, 1),
    (1111, 4),
    (13579, 5),
    (24680, 0),
]

ids = ["odd_num(%s) => %s" % (num, expected) for (num, expected) in params]


@pytest.mark.parametrize(argnames="num, expected", argvalues=params, ids=ids)
def test_count_odd_num(num, expected):
    assert count_odd_num(num) == expected
