import pytest

from topic_2_syntax.practice.string_2_print_3th_symbols import print_3th_symbols

params = [
    ('', ''),
    ('1', ''),
    ('12', ''),
    ('123', '3'),
    ('1234', '3'),
    ('12345', '3'),
    ('123456', '36'),
    ('123456789', '369'),
]

ids = ["string='%s' => '%s'" % (string, expected) for (string, expected) in params]


@pytest.mark.parametrize(argnames="string, expected", argvalues=params, ids=ids)
def test_print_3th_symbols(capsys, string, expected):
    print_3th_symbols(string)
    out, err = capsys.readouterr()
    assert out == expected + '\n'
