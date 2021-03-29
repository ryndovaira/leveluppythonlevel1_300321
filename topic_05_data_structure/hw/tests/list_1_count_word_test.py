import pytest

from topic_05_data_structure.hw.list_1_count_word import count_word

params = [
    (None, 0, 'First arg must be list!'),
    (0, 0, 'First arg must be list!'),
    (0.12, 0, 'First arg must be list!'),
    ('0', 0, 'First arg must be list!'),
    ((0, 1, 2), 0, 'First arg must be list!'),
    ({1: 2, 3: 4}, 0, 'First arg must be list!'),
    (None, 0, 'First arg must be list!'),
    ([], 0, 'Second arg must be str!'),
    ([], None, 'Second arg must be str!'),
    ([], [], 'Second arg must be str!'),

    ([], 'w', 'Empty list!'),

    ([1, 2, 3, 4], '1', 0),
    ([1, 2, 3, '1', 4], '1', 1),
    (["1", 2, 3, '1', 4], '1', 2),
    (["1", 2, 3, '1', 4, ''], '', 1),
    (["qwe2", 2, 3, '1qwe2', 4, 'qwe2'], 'qwe2', 2),
]

ids = ["list: %s | word: %s => %s" % (my_list, word, expected) for (my_list, word, expected) in params]


@pytest.mark.parametrize(argnames="my_list, word, expected",
                         argvalues=params,
                         ids=ids)
def test_count_word(my_list, word, expected):
    assert count_word(my_list, word) == expected



