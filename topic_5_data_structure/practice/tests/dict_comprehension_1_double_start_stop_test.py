import pytest

from topic_5_data_structure.practice.dict_comprehension_1_double_start_stop import double_start_stop

params = [
    ([], 1, 'Start and Stop must be int!'),
    (1, '1', 'Start and Stop must be int!'),
    ('1', '1', 'Start and Stop must be int!'),

    (0, 0, {}),
    (-1, 0, {-1: -2}),
    (-3, 3, {-3: -6, -2: -4, -1: -2, 0: 0, 1: 2, 2: 4}),

    (-3, -6, {}),
    (0, -6, {}),

    (0, 1, {0: 0}),
    (0, 2, {0: 0, 1: 2}),
    (0, 3, {0: 0, 1: 2, 2: 4}),
    (4, 9, {4: 8, 5: 10, 6: 12, 7: 14, 8: 16}),

]

ids = ["start=%s | stop=%s => %s" % (start, stop, expected) for (start, stop, expected) in params]


@pytest.mark.parametrize(argnames="start, stop, expected",
                         argvalues=params,
                         ids=ids)
def test_double_start_stop(start, stop, expected):
    assert double_start_stop(start, stop) == expected



