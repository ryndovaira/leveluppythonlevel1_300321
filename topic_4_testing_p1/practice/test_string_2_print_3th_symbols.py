from topic_2_syntax.practice.string_2_print_3th_symbols import print_3th_symbols


def test_string_2_print_3th_symbols_ep_ok(capsys):
    print_3th_symbols('qwertyuiop')
    out, err = capsys.readouterr()  # считываю потоки out и err
    assert out == 'eyo\n'

    print_3th_symbols('asd')
    out, err = capsys.readouterr()
    assert out == 'd\n'


def test_string_2_print_3th_symbols_bv(capsys):
    print_3th_symbols('')
    out, err = capsys.readouterr()
    assert out == '\n'

    print_3th_symbols('ab')
    out, err = capsys.readouterr()
    assert out == '\n'
