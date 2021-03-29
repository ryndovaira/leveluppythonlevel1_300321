import pytest

from topic_05_data_structure.hw.list_comprehension_1_pow_start_stop import pow_start_stop

params = [
    ([], 1, 'Start and Stop must be int!'),
    (1, '1', 'Start and Stop must be int!'),
    ('1', '1', 'Start and Stop must be int!'),

    (0, 0, []),
    (3, 6, [9, 16, 25]),
    (-3, -6, []),
    (-6, -3, [36, 25, 16]),
]

ids = ["start=%s | stop=%s => %s" % (start, stop, expected) for (start, stop, expected) in params]


@pytest.mark.parametrize(argnames="start, stop, expected",
                         argvalues=params,
                         ids=ids)
def test_pow_start_stop(start, stop, expected):
    assert pow_start_stop(start, stop) == expected



