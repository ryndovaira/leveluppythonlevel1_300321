import pytest

from topic_2_syntax.hw.loop_1_print_hi import print_hi


@pytest.mark.parametrize("n", [-10, -1, 0, 1, 2, 50])
def test_print_hi(capsys, n):
    expected = f'{n * "Hi, friend!"}\n'
    print_hi(n)
    out, err = capsys.readouterr()
    assert out == expected
