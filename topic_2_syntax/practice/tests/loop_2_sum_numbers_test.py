import pytest

from topic_2_syntax.practice.loop_2_sum_numbers import sum_numbers

params = [
    ('', None),
    ('-1', None),
    ('1 2', None),
    ('13!', None),
    ('7.54', None),

    ('010101', 3),
    ('123', 6),
    ('0', 0),
    ('000', 0),
    ('913746', 30),
]

ids = ["sum_numbers('%s') => %s" % (string, expected) for (string, expected) in params]


@pytest.mark.parametrize(argnames="string, expected", argvalues=params, ids=ids)
def test_sum_numbers(string, expected):
    assert sum_numbers(string) == expected
