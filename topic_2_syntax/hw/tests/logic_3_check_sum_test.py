import pytest

from topic_2_syntax.hw.logic_3_check_sum import check_sum

params = [
    (0, 0, 0, True),
    (1, -1, 0, True),
    (1, 0, -1, True),
    (0, 1, -1, True),
    (99, 0, 99, True),
    (1, 1, 1, False),
]

ids = ["(%s) ? (%s) ? (%s) => %s" % (num1, num2, num3, expected) for (num1, num2, num3, expected) in params]


@pytest.mark.parametrize(argnames="num1, num2, num3, expected", argvalues=params, ids=ids)
def test_check_sum(num1, num2, num3, expected):
    assert check_sum(num1, num2, num3) == expected
