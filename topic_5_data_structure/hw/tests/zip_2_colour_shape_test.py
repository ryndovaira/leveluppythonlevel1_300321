import pytest

from topic_5_data_structure.hw.zip_2_colour_shape import zip_colour_shape

params = [
    (None, None, 'First arg must be list!'),
    (0, (1, 2, 3), 'First arg must be list!'),
    ('0', (1, 2, 3), 'First arg must be list!'),

    ([], None, 'Second arg must be tuple!'),
    ([], 0, 'Second arg must be tuple!'),
    ([], '0', 'Second arg must be tuple!'),


    ([], (), 'Empty list!'),
    ([1], (), 'Empty tuple!'),

    (['Rose'], ('Circle',), [('Rose', 'Circle')]),
    (['Rose'], ('Circle', 'Triangle'), [('Rose', 'Circle')]),
    (['Rose', 'Pink'], ('Circle', 'Triangle'), [('Rose', 'Circle'), ('Pink', 'Triangle')]),
]

ids = ["colour_list: %s | shape_tuple: %s => %s" % (colour_list, shape_tuple, expected) for (colour_list, shape_tuple, expected) in params]


@pytest.mark.parametrize(argnames="colour_list, shape_tuple, expected",
                         argvalues=params,
                         ids=ids)
def test_zip_colour_shape(colour_list, shape_tuple, expected):
    assert zip_colour_shape(colour_list, shape_tuple) == expected

