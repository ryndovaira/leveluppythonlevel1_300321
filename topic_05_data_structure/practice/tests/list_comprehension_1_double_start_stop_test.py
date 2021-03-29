import pytest

from topic_05_data_structure.practice.list_comprehension_1_double_start_stop import double_start_stop

params = [
    ([], 1, 'Start and Stop must be int!'),
    (1, '1', 'Start and Stop must be int!'),
    ('1', '1', 'Start and Stop must be int!'),

    (0, 0, []),
    (3, 6, [6, 8, 10]),
    (-3, -6, []),
    (-6, -3, [-12, -10, -8]),
]

ids = ["start=%s | stop=%s => %s" % (start, stop, expected) for (start, stop, expected) in params]


@pytest.mark.parametrize(argnames="start, stop, expected",
                         argvalues=params,
                         ids=ids)
def test_double_start_stop(start, stop, expected):
    assert double_start_stop(start, stop) == expected



