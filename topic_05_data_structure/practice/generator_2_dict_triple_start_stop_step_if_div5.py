"""
Функция dict_triple_start_stop_step_if_div5.

Принимает 3 аргумента: числа start, stop, step.

Возвращает генератор-выражение состоящий из кортежа (аналог dict):
(значение, утроенное значение)
при этом значения перебираются от start до stop (не включая) с шагом step
только для чисел, которые делятся на 5 без остатка.

Пример: start=0, stop=16, step=1
результат ((0, 0), (5, 15), (10, 30), (15, 45)).

Если start или stop или step не являются int, т
о вернуть строку 'Start and Stop and Step must be int!'.

Если step равен 0, то вернуть строку "Step can't be zero!"
"""


def dict_triple_start_stop_step_if_div5(start, stop, step):
    if type(start) != int or type(stop) != int or type(step) != int:
        return 'Start and Stop and Step must be int!'

    if step == 0:
        return "Step can't be zero!"

    return ((x, x * 3) for x in range(start, stop, step) if x % 5 == 0)
