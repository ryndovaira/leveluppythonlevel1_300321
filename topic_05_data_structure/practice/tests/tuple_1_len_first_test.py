import pytest

from topic_05_data_structure.practice.tuple_1_len_first import len_first

params = [
    ([], 'Must be tuple!'),
    (tuple(), 'Empty tuple!'),
    (('55',), (1, '55')),
    (('55', 'aa', 66), (3, '55')),
]

ids = ["tuple: %s => %s" % (test_tuple, expected) for (test_tuple, expected) in params]


@pytest.mark.parametrize(argnames="test_tuple, expected",
                         argvalues=params,
                         ids=ids)
def test_len_first(test_tuple, expected):
    assert len_first(test_tuple) == expected
