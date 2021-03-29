import pytest

from topic_02_syntax.hw.string_1_print_symbols_if import print_symbols_if

params = [
    ('123456789', '123789'),
    ('123789', '123789'),
    ('01238', '00000'),
    ('1234', '1111'),
    ('222', '222'),
    ('33', '33'),
    ('4', '4'),
    ('', "Empty string!"),
]

ids = ["(%s) => (%s)" % (string, expected) for (string, expected) in params]


@pytest.mark.parametrize(argnames="string, expected", argvalues=params, ids=ids)
def test_print_symbols_if(capsys, string, expected):
    print_symbols_if(string)
    out, err = capsys.readouterr()
    assert out == expected + '\n'
