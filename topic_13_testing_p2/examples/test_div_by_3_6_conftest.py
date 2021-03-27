# Чтобы получить доступ к фикстуре, тесты должны упомянуть имя фикстуры в качестве входного параметра
import pytest


@pytest.mark.xfail
def test_divisible_by_3(input_value):
    assert input_value % 3 == 0


# Чтобы получить доступ к фикстуре, тесты должны упомянуть имя фикстуры в качестве входного параметра
@pytest.mark.xfail  # падает и это нормально!
def test_divisible_by_6(input_value):
    assert input_value % 6 == 0
