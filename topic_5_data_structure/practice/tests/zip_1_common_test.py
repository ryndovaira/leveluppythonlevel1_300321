import pytest

from topic_5_data_structure.practice.zip_1_common import zip_common

params = [
    (None, "", (), 'First arg must be list!'),
    ([], None, (), 'Second arg must be str!'),
    ([], "", None, 'Third arg must be tuple!'),

    ([], "", (), 'Empty list!'),
    ([1], "", (), 'Empty str!'),
    ([1], "1", (), 'Empty tuple!'),

    (['Rose'], 'B', ('Pink',), [('Rose', 'B', 'Pink')]),
    (['Rose', 'Blue'], 'B', ('Pink',), [('Rose', 'B', 'Pink')]),
    (['Rose'], 'Ba', ('Pink',), [('Rose', 'B', 'Pink')]),
    (['Rose'], 'B', ('Pink', 'Green'), [('Rose', 'B', 'Pink')]),

    (['Rose', 'Blue', 'White'],
     'Boo',
     ('Pink', 'Green', 'Rainbow'),
     [('Rose', 'B', 'Pink'),
      ('Blue', 'o', 'Green'),
      ('White', 'o', 'Rainbow')]),
]

ids = [f"list: {my_list} | str: {my_str} | tuple: {my_tuple} => {expected}"
       for (my_list, my_str, my_tuple, expected) in params]


@pytest.mark.parametrize(argnames="my_list, my_str, my_tuple, expected",
                         argvalues=params,
                         ids=ids)
def test_zip_common(my_list, my_str, my_tuple, expected):
    if type(expected) == str:
        assert zip_common(my_list, my_str, my_tuple) == expected
    else:
        result = zip_common(my_list, my_str, my_tuple)
        assert len(result) == len(expected)
        for exp_item in expected:
            assert exp_item in result


