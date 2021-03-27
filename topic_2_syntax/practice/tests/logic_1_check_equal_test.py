import pytest

from topic_2_syntax.practice.logic_1_check_equal import check_equal


@pytest.mark.parametrize("num1, num2, num3, output", [
    (1, 2, 3, False),
    (1, 1, 2, True),
    (3, 4, 4, True),
    (5, 6, 5, True),
    (7, 7, 7, True),
    (66, 66, 66, True)
])
def test_check_eq(num1, num2, num3, output):
    assert check_equal(num1, num2, num3) == output
