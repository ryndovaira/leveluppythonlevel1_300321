import pytest

from topic_05_data_structure.hw.dict_comprehension_1_pow_start_stop import pow_start_stop

params = [
    ([], 1, 'Start and Stop must be int!'),
    (1, '1', 'Start and Stop must be int!'),
    ('1', '1', 'Start and Stop must be int!'),

    (0, 0, {}),
    (-1, 0, {-1: 1}),
    (-3, 3, {-3: 9, -2: 4, -1: 1, 0: 0, 1: 1, 2: 4}),

    (-3, -6, {}),
    (0, -6, {}),

    (0, 1, {0: 0}),
    (0, 2, {0: 0, 1: 1}),
    (0, 3, {0: 0, 1: 1, 2: 4}),
    (4, 9, {4: 16, 5: 25, 6: 36, 7: 49, 8: 64}),

]

ids = ["start=%s | stop=%s => %s" % (start, stop, expected) for (start, stop, expected) in params]


@pytest.mark.parametrize(argnames="start, stop, expected",
                         argvalues=params,
                         ids=ids)
def test_pow_start_stop(start, stop, expected):
    assert pow_start_stop(start, stop) == expected



