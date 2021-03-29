import pytest

from topic_05_data_structure.practice.zip_2_name_mark import zip_name_mark

params = [
    (None, [], 'Both args must be list and not empty!'),
    ([], None, 'Both args must be list and not empty!'),

    ([], [1], 'Both args must be list and not empty!'),
    ([""], [], 'Both args must be list and not empty!'),

    ([1], [1], 'Names must be str!'),
    (["Ira", "Kate", 8], [90, 95, 100], 'Names must be str!'),

    (["Ira"], [-1], 'Marks must be int (0 to 100)!'),
    (["Ira"], [101], 'Marks must be int (0 to 100)!'),
    (["Ira"], [-150], 'Marks must be int (0 to 100)!'),
    (["Ira"], [150], 'Marks must be int (0 to 100)!'),
    (["Ira", "Kate"], [90, 95, -50], 'Marks must be int (0 to 100)!'),

    (["Ira", "Kate", 'Ivan'], [0, 100, 50], [('Ira', 0), ('Kate', 100), ('Ivan', 50)]),
    (["Ira", "Kate", 'Ivan'], [0, 100], [('Ira', 0), ('Kate', 100), ('Ivan', '!!!')]),
    (["Ira", "Kate", ], [0, 100, 50], [('Ira', 0), ('Kate', 100), ('!!!', 50)]),

]

ids = [f"list: {name_list} | str: {mark_list} => {expected}"
       for (name_list, mark_list, expected) in params]


@pytest.mark.parametrize(argnames="name_list, mark_list, expected",
                         argvalues=params,
                         ids=ids)
def test_zip_name_mark(name_list, mark_list, expected):
    if type(expected) == str:
        assert zip_name_mark(name_list, mark_list) == expected
    else:
        result = zip_name_mark(name_list, mark_list)
        assert len(result) == len(expected)
        for exp_item in expected:
            assert exp_item in result


