import pytest

from topic_5_data_structure.hw.convert_1_list_to_dict import list_to_dict

params = [
    ([], 0, {}),

    ([0], 0, {0: (0, True, 1)}),

    ([0, 1, 2], 0, {0: (0, True, 3),
                    1: (1, False, 3),
                    2: (2, False, 3)}),

    (['a', 'bc', 'df'], 'f', {'a': (0, False, 3),
                              'bc': (1, False, 3),
                              'df': (2, False, 3)}),

    (['a', 'bc', None, 'df'], None, {None: (2, True, 4),
                                     'a': (0, False, 4),
                                     'bc': (1, False, 4),
                                     'df': (3, False, 4)}),

    (['a', 'bc', 'df', 'a'], 'a', {'a': (3, True, 3),
                                   'bc': (1, False, 3),
                                   'df': (2, False, 3)}),

    ([0, 0, 0], 0, {0: (2, True, 1)}),

    ([0, 0, 1], 0, {0: (1, True, 2),
                    1: (2, False, 2)}),

    ([1, 1, 1], '1', {1: (2, False, 1)}),

    ([0, 1, 2, 3], 'e', {0: (0, False, 4),
                         1: (1, False, 4),
                         2: (2, False, 4),
                         3: (3, False, 4)
                         }),


    (None, 0, 'First arg must be list!'),
    (0, 0, 'First arg must be list!'),
    (0.12, 0, 'First arg must be list!'),
    ('0', 0, 'First arg must be list!'),
    ((0, 1, 2), 0, 'First arg must be list!'),
    ({1: 2, 3: 4}, 0, 'First arg must be list!'),
    (None, 0, 'First arg must be list!'),
]

ids = ["list: %s | val: %s => %s" % (my_list, val, expected) for (my_list, val, expected) in params]


@pytest.mark.parametrize(argnames="my_list, val, expected",
                         argvalues=params,
                         ids=ids)
def test_list_to_dict(my_list, val, expected):
    assert list_to_dict(my_list, val) == expected



