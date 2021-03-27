import pytest


# функция фикстуры с именем input_value, которая предоставляет входные данные для тестов
@pytest.fixture
def input_value_local():
    input = 39
    return input


# Чтобы получить доступ к фикстуре, тесты должны упомянуть имя фикстуры в качестве входного параметра
def test_divisible_by_3(input_value_local):
    assert input_value_local % 3 == 0


# Чтобы получить доступ к фикстуре, тесты должны упомянуть имя фикстуры в качестве входного параметра
@pytest.mark.xfail
def test_divisible_by_6(input_value_local):
    assert input_value_local % 6 == 0
