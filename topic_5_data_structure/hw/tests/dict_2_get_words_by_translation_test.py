import pytest

from topic_5_data_structure.hw.dict_2_get_words_by_translation import get_words_by_translation

params = [
    ({}, "", "Dictionary is empty!"),
    ({"кот": ["cat"]}, "", "Word is empty!"),

    ([], "", "Dictionary must be dict!"),
    ("dict", "", "Dictionary must be dict!"),

    ({"кот": ["cat"]}, [], "Word must be str!"),
    ({"кот": ["cat"]}, None, "Word must be str!"),

    ({"кот": ["cat"]}, "dog", "Can't find English word: dog"),
    ({"кот": ["cat"]}, "cat", ["кот"]),

    ({
         "кошка": ["cat"], "ручка": ["pen", "hand"],
         "человек": ["human", "man", "person"],
         "мужчина": ["man"]
     },
     "human",
     ["человек"]),

    ({
         "кошка": ["cat"], "ручка": ["pen", "hand"],
         "человек": ["human", "man", "person"],
         "мужчина": ["man"]
     },
     "man",
     ["человек", "мужчина"]),

    ({
         "кошка": ["cat"], "ручка": ["pen", "hand"],
         "человек": ["human", "man", "person"],
         "мужчина": ["man"]
     },
     "hand",
     ["ручка"]),
]

ids = ["dict: %s | word: %s => %s" % (ru_eng_dict, val, expected) for (ru_eng_dict, val, expected) in params]


@pytest.mark.parametrize(argnames="ru_eng_dict, eng_word, expected",
                         argvalues=params,
                         ids=ids)
def test_get_words_by_translation(ru_eng_dict, eng_word, expected):
    assert get_words_by_translation(ru_eng_dict, eng_word) == expected


