import pytest

from topic_5_data_structure.hw.zip_3_car_year import zip_car_year

params = [
    (None, None, 'Must be list!'),
    (0, (1, 2, 3), 'Must be list!'),
    ('1', (1, 2, 3), 'Must be list!'),

    ([1], None, 'Must be list!'),
    ([1], 0, 'Must be list!'),
    ([1], '1', 'Must be list!'),


    ([], [1], 'Empty list!'),
    ([1], [], 'Empty list!'),

    (['Kia'], ['2000'], [('Kia', '2000')]),
    (['Kia'], ['2000', '2010'], [('Kia', '2000'), ('???', '2010')]),
    (['Kia', 'Nissan'], ['2010'], [('Kia', '2010'), ('Nissan', '???')]),
    (['Kia', 'Nissan'], ['2000', '2010'], [('Kia', '2000'), ('Nissan', '2010')]),
]

ids = ["car_list: %s | year_list: %s => %s" % (car_list, year_list, expected) for (car_list, year_list, expected) in params]


@pytest.mark.parametrize(argnames="car_list, year_list, expected",
                         argvalues=params,
                         ids=ids)
def test_zip_car_year(car_list, year_list, expected):
    assert zip_car_year(car_list, year_list) == expected


