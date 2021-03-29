import pytest

from topic_05_data_structure.practice.generator_1_pow3_start_inf_step import pow3_start_inf_step

params = [
    ([], 1, 'Start and Step must be int!'),
    (1, '1', 'Start and Step must be int!'),
    ('1', '1', 'Start and Step must be int!'),

    (-6, 2, [-216, -64, -8, 0]),
    (0, -1, [0, -1, -8, -27]),
    (1, 0, [1, 1, 1, 1]),
    (1, 1, [1, 8, 27, 64]),
    (1, 3, [1, 64, 343, 1000]),

]

ids = ["start=%s | step=%s => %s" % (start, step, expected)
       for (start, step, expected) in params]


@pytest.mark.parametrize(argnames="start, step, expected",
                         argvalues=params,
                         ids=ids)
def test_pow3_start_inf_step(start, step, expected):
    gen = pow3_start_inf_step(start, step)
    if type(gen) == str:
        assert gen == expected
    else:
        for next_expected in expected:
            assert next(gen) == next_expected
