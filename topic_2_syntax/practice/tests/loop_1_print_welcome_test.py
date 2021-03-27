import pytest

from topic_2_syntax.practice.loop_1_print_welcome import print_welcome


@pytest.mark.parametrize("n", [-10, -1, 0, 1, 2, 50])
def test_print_welcome(capsys, n):
    expected = f'{n * "You are welcome!"}\n'
    print_welcome(n)
    out, err = capsys.readouterr()
    assert out == expected
