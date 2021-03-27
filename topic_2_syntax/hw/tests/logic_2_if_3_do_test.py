import pytest

from topic_2_syntax.hw.logic_2_if_3_do import if_3_do

params = [
    (-3, -13),
    (0, -10),
    (2, -8),
    (2.9, -7.1),
    (3, -7),
    (3.00001, 13.00001),
    (3.5, 13.5),
    (3.99, 13.99),
    (4, 14),
]

ids = ["(%s) => (%s)" % (num, expected) for (num, expected) in params]


@pytest.mark.parametrize(argnames="num, expected", argvalues=params, ids=ids)
def test_if_3_do(num, expected):
    assert if_3_do(num) == expected
