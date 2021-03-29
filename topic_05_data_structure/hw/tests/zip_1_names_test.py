import pytest

from topic_05_data_structure.hw.zip_1_names import zip_names

params = [
    (None, None, 'First arg must be list!'),
    (0, (1, 2, 3), 'First arg must be list!'),
    ('0', (1, 2, 3), 'First arg must be list!'),

    ([], None, 'Second arg must be set!'),
    ([], 0, 'Second arg must be set!'),
    ([], '0', 'Second arg must be set!'),

    ([], set(), 'Empty list!'),
    ([1], set(), 'Empty set!'),

    (['Rose'], {'Black'}, [('Rose', 'Black')]),
    (['Rose'], {'Black', 'Pink'}, [('Rose', 'Black')]),
    (['Rose', 'Mark'], {'Black', 'Pink'}, [('Rose', 'Pink'), ('Mark', 'Black')]),
]

ids = ["name_list: %s | surname_set: %s => %s" % (name_list, surname_set, expected) for
       (name_list, surname_set, expected) in params]


def unpack_zipped_list(zipped_list: list):
    all_items = []
    for tuple_tmp in zipped_list:
        for item in tuple_tmp:
            all_items.append(item)
    return all_items


@pytest.mark.parametrize(argnames="name_list, surname_set, expected",
                         argvalues=params,
                         ids=ids)
def test_zip_names(name_list, surname_set, expected):
    if type(expected) == str:
        assert zip_names(name_list, surname_set) == expected
    else:
        result = zip_names(name_list, surname_set)
        assert len(result) == len(expected)

        all_expected = unpack_zipped_list(expected)
        all_results = unpack_zipped_list(result)

        for exp_item in all_expected:
            assert exp_item in all_results
