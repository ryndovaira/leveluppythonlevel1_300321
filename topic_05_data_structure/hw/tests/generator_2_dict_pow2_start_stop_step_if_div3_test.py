import pytest

from topic_05_data_structure.hw.generator_2_dict_pow2_start_stop_step_if_div3 import dict_pow2_start_stop_step_if_div3

params = [
    (None, 1, 1, 'Start and Stop and Step must be int!'),
    (1, None, 1, 'Start and Stop and Step must be int!'),
    (1, 1, None, 'Start and Stop and Step must be int!'),
    ('1', 1, 1, 'Start and Stop and Step must be int!'),
    (1, '1', 1, 'Start and Stop and Step must be int!'),
    (1, 1, '1', 'Start and Stop and Step must be int!'),
    ('1', '1', '1',  'Start and Stop and Step must be int!'),

    (0, 0, 0, "Step can't be zero!"),
    (0, 10, 1, ((0, 0), (3, 9), (6, 36), (9, 81))),
    (-9, 9, 1, ((-9, 81), (-6, 36), (-3, 9), (0, 0), (3, 9), (6, 36))),
]

ids = ["start=%s | stop=%s | step=%s => %s" % (start, stop, step, expected)
       for [start, stop, step, expected] in params]


@pytest.mark.parametrize(argnames="start, stop, step, expected",
                         argvalues=params,
                         ids=ids)
def test_dict_pow2_start_stop_step_if_div3(start, stop, step, expected):
    gen = dict_pow2_start_stop_step_if_div3(start, stop, step)
    if type(gen) == str:
        assert gen == expected
    else:
        for next_expected in expected:
            assert next(gen) == next_expected
