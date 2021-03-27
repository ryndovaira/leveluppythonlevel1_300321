import pytest

from topic_2_syntax.hw.string_2_print_nth_symbols import print_nth_symbols

params = [
    ('123456789', [], 'Must be int!'),
    ('123456789', True, 'Must be int!'),
    ('123456789', '1.23', 'Must be int!'),
    ('123456789', 3.23, 'Must be int!'),
    ('123456789', -1.23, 'Must be int!'),
    ('123456789', 0, 'Must be > 0!'),
    ('123456789', -1, 'Must be > 0!'),
    ('123456789', 1, '23456789'),
    ('123456789', 2, '3579'),
    ('123456789', 3, '47'),
    ('123456789', 5, '6'),
    ('123456789', 6, '7'),
    ('123456789', 7, '8'),
    ('123456789', 8, '9'),
    ('123456789', 9, ''),
    ('123456789qwertyuiop', 2, '3579wryip'),
]

ids = ["string='%s' | n=%s => '%s'" % (string, n, expected) for (string, n, expected) in params]


@pytest.mark.parametrize(argnames="string, n, expected", argvalues=params, ids=ids)
def test_print_nth_symbols(capsys, string, n, expected):
    print_nth_symbols(string, n)
    out, err = capsys.readouterr()
    assert out == expected + '\n'
