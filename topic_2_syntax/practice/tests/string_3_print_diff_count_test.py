import pytest

from topic_2_syntax.practice.string_3_print_diff_count import print_diff_count

params = [
    ('', '', 'Equal!'),
    ('1', '1', 'Equal!'),
    ('123', '123', 'Equal!'),
    ('', '123', '123123123'),
    ('123', '', '123123123'),
    ('1', '', '1'),
    ('12', '', '1212'),
    ('12', '12345', '123451234512345'),
]

ids = ["'%s' | '%s' => '%s'" % (str1, str2, expected) for (str1, str2, expected) in params]


@pytest.mark.parametrize(argnames="str1, str2, expected", argvalues=params, ids=ids)
def test_print_diff_count(capsys, str1, str2, expected):
    print_diff_count(str1, str2)
    out, err = capsys.readouterr()
    assert out == expected + '\n'
