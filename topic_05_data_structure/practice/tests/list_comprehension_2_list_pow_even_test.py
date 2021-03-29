import pytest

from topic_05_data_structure.practice.list_comprehension_2_list_pow_even import list_pow_even

params = [
    ([], 'Must be int!'),
    (None, 'Must be int!'),
    ('1', 'Must be int!'),

    (-3, []),
    (0, []),
    (1, [0]),
    (2, [0]),
    (3, [0, 4]),
    (4, [0, 4]),
    (5, [0, 4, 16]),
    (6, [0, 4, 16]),
    (7, [0, 4, 16, 36]),
]

ids = ["n=%s => %s" % (n, expected) for (n, expected) in params]


@pytest.mark.parametrize(argnames="n, expected",
                         argvalues=params,
                         ids=ids)
def test_list_pow_even(n, expected):
    assert list_pow_even(n) == expected



