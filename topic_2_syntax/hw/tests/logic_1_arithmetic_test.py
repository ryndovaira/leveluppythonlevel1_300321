import pytest

from topic_2_syntax.hw.logic_1_arithmetic import arithmetic

params = [
    (0, 0, '+', 0),
    (1, 0, '+', 1),
    (0, 1, '+', 1),
    (100, 100, '+', 200),
    (100, -100, '+', 0),
    (-100, 100, '+', 0),
    (-100, -100, '+', -200),

    (0, 0, '-', 0),
    (1, 0, '-', 1),
    (0, 1, '-', -1),
    (100, 100, '-', 0),
    (100, -100, '-', 200),
    (-100, 100, '-', -200),
    (-100, -100, '-', 0),

    (0, 0, '*', 0),
    (1, 0, '*', 0),
    (0, 1, '*', 0),
    (100, 100, '*', 10000),
    (100, -100, '*', -10000),
    (-100, 100, '*', -10000),
    (-100, -100, '*', 10000),

    (0, 1, '/', 0),
    (1, 1, '/', 1),
    (100, 100, '/', 1),
    (100, -100, '/', -1),
    (-100, 100, '/', -1),
    (-100, -100, '/', 1),

    (0, 1, '=', "Unknown operator"),
    (1, 1, '%', "Unknown operator"),
    (100, 100, '#', "Unknown operator"),
    (100, -100, '.', "Unknown operator"),
    (-100, 100, '0', "Unknown operator"),
    (-100, -100, '&', "Unknown operator"),
]

ids = ["(%s) %s (%s) == (%s)" % (num1, op, num2, expected) for (num1, num2, op, expected) in params]


@pytest.mark.parametrize(argnames="num1, num2, op, expected",
                         argvalues=params,
                         ids=ids)
def test_arithmetic(num1, num2, op, expected):
    assert arithmetic(num1, num2, op) == expected
