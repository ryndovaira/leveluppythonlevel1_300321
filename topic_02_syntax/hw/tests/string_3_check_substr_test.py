import pytest

from topic_02_syntax.hw.string_3_check_substr import check_substr

params = [
    ('', '', False),
    ('', 'o', True),
    ('aaa', 'aaa', False),
    ('b', 'bbb', True),
    ('bb', 'bbb', True),
    ('ccc', 'c', True),
    ('ccc', 'cc', True),
    ('qwe', 'q', True),
    ('qwe', 'w', True),
    ('qwe', 'e', True),
    ('qwe', 'we', True),
    ('qwe', 'qe', False),
]

ids = ["str1='%s' ? str2=%s => '%s'" % (str1, str2, expected) for (str1, str2, expected) in params]


@pytest.mark.parametrize(argnames="str1, str2, expected", argvalues=params, ids=ids)
def test_check_substr(str1, str2, expected):
    assert check_substr(str1, str2) == expected
