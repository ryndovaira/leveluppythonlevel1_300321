import pytest

from topic_5_data_structure.hw.generator_1_pow5_start_inf_step import pow5_start_inf_step

params = [
    ([], 1, 'Start and Step must be int!'),
    (1, '1', 'Start and Step must be int!'),
    ('1', '1', 'Start and Step must be int!'),

    (-6, 2, [-7776, -1024, -32, 0]),
    (0, -1, [0, -1, -32, -243]),
    (1, 0, [1, 1, 1, 1]),
    (1, 1, [1, 32, 243, 1024]),
    (1, 3, [1, 1024, 16807, 100000]),

]

ids = ["start=%s | step=%s => %s" % (start, step, expected)
       for (start, step, expected) in params]


@pytest.mark.parametrize(argnames="start, step, expected",
                         argvalues=params,
                         ids=ids)
def test_pow5_start_inf_step(start, step, expected):
    gen = pow5_start_inf_step(start, step)
    if type(gen) == str:
        assert gen == expected
    else:
        for next_expected in expected:
            assert next(gen) == next_expected
