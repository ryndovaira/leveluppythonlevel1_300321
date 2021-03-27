import pytest

from topic_2_syntax.practice.string_1_triple_string_len import triple_string_len

params = [
    ('', None),
    ('W', "W, W? W! len=1 :)"),
    ('WoW', "WoW, WoW? WoW! len=3 :)"),
    ('-*#*-', "-*#*-, -*#*-? -*#*-! len=5 :)"),
]

ids = ["'%s' => %s" % (string, expected) for (string, expected) in params]


@pytest.mark.parametrize(argnames="string, expected", argvalues=params, ids=ids)
def test_triple_string_len(string, expected):
    assert triple_string_len(string) == expected
