import pytest

from topic_5_data_structure.hw.dict_comprehension_2_pow_odd import pow_odd

params = [
    ([], 'Must be int!'),
    (None, 'Must be int!'),
    ('1', 'Must be int!'),

    (-3, {}),
    (0, {}),

    (1, {1: 1}),

    (4, {1: 1, 3: 9}),
    (5, {1: 1, 3: 9, 5: 25}),
    (6, {1: 1, 3: 9, 5: 25}),
]

ids = ["n=%s => %s" % (n, expected) for (n, expected) in params]


@pytest.mark.parametrize(argnames="n, expected",
                         argvalues=params,
                         ids=ids)
def test_pow_odd(n, expected):
    assert pow_odd(n) == expected



