import pytest

from topic_05_data_structure.practice.convert_1_set_to_dict import set_to_dict

params = [
    (set(), 0, {}),
    ({0}, 0, {0: (True, 1)}),

    ({0, 1, 2}, 0, {0: (True, 3),
                    1: (False, 3),
                    2: (False, 3)}),

    ({'a', 'bc', 'df'}, 'f', {'a': (False, 3),
                              'bc': (False, 3),
                              'df': (False, 3)}),

    ({'a', 'bc', None, 'df'}, None, {None: (True, 4),
                                     'a': (False, 4),
                                     'bc': (False, 4),
                                     'df': (False, 4)}),

    ({'a', 'bc', 'df', 'a'}, 'a', {'a': (True, 3),
                                   'bc': (False, 3),
                                   'df': (False, 3)}),

    ({0, 0, 0}, 0, {0: (True, 1)}),

    ({0, 0, 1}, 0, {0: (True, 2),
                    1: (False, 2)}),

    ({1, 1, 1}, '1', {1: (False, 1)}),

    ({0, 1, 2, 3}, 'e', {0: (False, 4),
                         1: (False, 4),
                         2: (False, 4),
                         3: (False, 4)
                         }),


    (None, 0, 'First arg must be set!'),
    (0, 0, 'First arg must be set!'),
    (0.12, 0, 'First arg must be set!'),
    ('0', 0, 'First arg must be set!'),
    ((0, 1, 2), 0, 'First arg must be set!'),
    ({1: 2, 3: 4}, 0, 'First arg must be set!'),
    (None, 0, 'First arg must be set!'),
]

ids = ["set: %s | val: %s => %s" % (my_set, val, expected) for (my_set, val, expected) in params]


@pytest.mark.parametrize(argnames="my_set, val, expected",
                         argvalues=params,
                         ids=ids)
def test_set_to_dict(my_set, val, expected):
    assert set_to_dict(my_set, val) == expected



