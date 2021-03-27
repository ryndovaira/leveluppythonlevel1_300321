import pytest

from topic_2_syntax.practice.logic_2_swap import swap


@pytest.mark.parametrize("first_param, second_param", [
    (1, 2),
    ('abc', 1),
    (3, 'qwe'),
    ('rty', 'B'),
    ('', None),
    (3.467, False)
])
def test_swap(capsys, first_param, second_param):
    expected = f"first_param = {second_param} | second_param = {first_param}\n"
    swap(first_param, second_param)
    out, err = capsys.readouterr()  # считываю потоки out и err
    assert out == expected
