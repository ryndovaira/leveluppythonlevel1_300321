import pytest

from topic_02_syntax.practice.logic_0_season import season

params = [
    (12, 'Winter'),
    (1, 'Winter'),
    (2, 'Winter'),
    (3, 'Spring'),
    (4, 'Spring'),
    (5, 'Spring'),
    (6, 'Summer'),
    (7, 'Summer'),
    (8, 'Summer'),
    (9, 'Fall'),
    (10, 'Fall'),
    (11, 'Fall'),

    (0, None),
    (13, None),
    (345, None),
]

ids = ["month=%s => %s" % (month, expected) for (month, expected) in params]


@pytest.mark.parametrize(argnames="month, expected", argvalues=params, ids=ids)
def test_season(month, expected):
    assert season(month) == expected

