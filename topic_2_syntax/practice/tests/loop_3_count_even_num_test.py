import pytest

from topic_2_syntax.practice.loop_3_count_even_num import count_even_num

params = [
    (1.23, "Must be int!"),
    (-1.34, "Must be int!"),
    ("5", "Must be int!"),
    (True, "Must be int!"),
    (-5, "Must be > 0!"),
    (0, "Must be > 0!"),
    (1, 0),
    (2, 1),
    (4, 1),
    (10, 1),
    (1111, 0),
    (222222, 6),
    (13579, 0),
    (24680, 5),
]

ids = ["even_num(%s) => %s" % (num, expected) for (num, expected) in params]


@pytest.mark.parametrize(argnames="num, expected", argvalues=params, ids=ids)
def test_count_even_num(num, expected):
    assert count_even_num(num) == expected
