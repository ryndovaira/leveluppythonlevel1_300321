import pytest

from topic_5_data_structure.practice.generator_2_dict_triple_start_stop_step_if_div5 import dict_triple_start_stop_step_if_div5

params = [
    (None, 1, 1, 'Start and Stop and Step must be int!'),
    (1, None, 1, 'Start and Stop and Step must be int!'),
    (1, 1, None, 'Start and Stop and Step must be int!'),
    ('1', 1, 1, 'Start and Stop and Step must be int!'),
    (1, '1', 1, 'Start and Stop and Step must be int!'),
    (1, 1, '1', 'Start and Stop and Step must be int!'),
    ('1', '1', '1',  'Start and Stop and Step must be int!'),

    (0, 0, 0, "Step can't be zero!"),
    (0, 16, 1, ((0, 0), (5, 15), (10, 30), (15, 45))),
    (-9, 9, 1, ((-5, -15), (0, 0), (5, 15))),
]

ids = ["start=%s | stop=%s | step=%s => %s" % (start, stop, step, expected)
       for [start, stop, step, expected] in params]


@pytest.mark.parametrize(argnames="start, stop, step, expected",
                         argvalues=params,
                         ids=ids)
def test_dict_triple_start_stop_step_if_div5(start, stop, step, expected):
    gen = dict_triple_start_stop_step_if_div5(start, stop, step)
    if type(gen) == str:
        assert gen == expected
    else:
        for next_expected in expected:
            assert next(gen) == next_expected
