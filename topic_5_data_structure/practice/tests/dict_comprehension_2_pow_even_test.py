import pytest

from topic_5_data_structure.practice.dict_comprehension_2_pow_even import pow_even

params = [
    ([], 'Must be int!'),
    (None, 'Must be int!'),
    ('1', 'Must be int!'),

    (-3, {}),
    (0, {}),

    (1, {0: 0}),

    (4, {0: 0, 2: 4}),
    (5, {0: 0, 2: 4, 4: 16}),
    (6, {0: 0, 2: 4, 4: 16}),
]

ids = ["n=%s => %s" % (n, expected) for (n, expected) in params]


@pytest.mark.parametrize(argnames="n, expected",
                         argvalues=params,
                         ids=ids)
def test_pow_even(n, expected):
    assert pow_even(n) == expected



