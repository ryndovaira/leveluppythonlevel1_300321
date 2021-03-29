import pytest

from topic_05_data_structure.hw.tuple_1_len_count_first import len_count_first

params = [
    (None, 0, 'First arg must be tuple!'),
    (0, 0, 'First arg must be tuple!'),
    (0.12, 0, 'First arg must be tuple!'),
    ('0', 0, 'First arg must be tuple!'),
    ([0, 1, 2], 0, 'First arg must be tuple!'),
    ({1: 2, 3: 4}, 0, 'First arg must be tuple!'),
    (None, 0, 'First arg must be tuple!'),
    ((), 0, 'Second arg must be str!'),
    ((), None, 'Second arg must be str!'),
    ((), [], 'Second arg must be str!'),

    ((), 'w', 'Empty tuple!'),

    ((1, 2, 3, 4), '1', (4, 0, 1)),
    ((1, 2, 3, '1', 4), '1', (5, 1, 1)),
    (("1", 2, 3, '1', 4), '1', (5, 2, '1')),
    (("1", 2, 3, '1', 4, ''), '', (6, 1, '1')),
    (("qwe2", 2, 3, '1qwe2', 4, 'qwe2'), 'qwe2', (6, 2, 'qwe2')),
    (('55', 'aa', '66'), '66', (3, 1, '55')),
]

ids = ["tuple: %s | word: %s => %s" % (my_tuple, word, expected) for (my_tuple, word, expected) in params]


@pytest.mark.parametrize(argnames="my_tuple, word, expected",
                         argvalues=params,
                         ids=ids)
def test_len_count_first(my_tuple, word, expected):
    assert len_count_first(my_tuple, word) == expected



