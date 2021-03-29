import pytest

from topic_02_syntax.practice.logic_3_check_numbers_by_5 import check_numbers_by_5

params = [
    (0, 0, 6, True),
    (0, 1, 6, True),
    (-1, -6, 8, True),
    (3, 1, 6, True),
    (4, 4, 5, True),
    (4, 5, 4, True),
    (5, 4, 4, True),
    (5, 1, 5, False),
    (5, 5, 1, False),
    (1, 5, 5, False),
    (2, 6, 6, False),
]

ids = ["(%s) ? (%s) ? (%s) => %s" % (num1, num2, num3, expected) for (num1, num2, num3, expected) in params]


@pytest.mark.parametrize(argnames="num1, num2, num3, expected", argvalues=params, ids=ids)
def test_check_numbers_by_5(num1, num2, num3, expected):
    assert check_numbers_by_5(num1, num2, num3) == expected
