import pytest

from topic_5_data_structure.hw.dict_1_get_translation_by_word import get_translation_by_word

params = [
    ({}, "", "Dictionary is empty!"),
    ({"кот": ["cat"]}, "", "Word is empty!"),

    ([], "", "Dictionary must be dict!"),
    ("dict", "", "Dictionary must be dict!"),

    ({"кот": ["cat"]}, [], "Word must be str!"),
    ({"кот": ["cat"]}, None, "Word must be str!"),

    ({"кот": ["cat"]}, "собака", "Can't find Russian word: собака"),
    ({"кот": ["cat"]}, "кот", ["cat"]),
    ({"кот": ["cat"], "человек": ["man", "human", "person"]}, "человек", ["man", "human", "person"]),
]

ids = ["dict: %s | word: %s => %s" % (ru_eng_dict, val, expected) for (ru_eng_dict, val, expected) in params]


@pytest.mark.parametrize(argnames="ru_eng_dict, ru_word, expected",
                         argvalues=params,
                         ids=ids)
def test_get_translation_by_word(ru_eng_dict, ru_word, expected):
    assert get_translation_by_word(ru_eng_dict, ru_word) == expected


