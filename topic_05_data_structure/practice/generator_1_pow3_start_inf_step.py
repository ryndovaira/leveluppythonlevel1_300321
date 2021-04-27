"""
Функция pow3_start_inf_step.

Принимает 2 аргумента: число start, step.

Возвращает генератор-выражение состоящий из
значений в 3 степени от start до бесконечности с шагом step.

Пример: start=3, step=2 результат 3^3, 5^3, 7^3, 9^3 ... (infinity).

Если start или step не являются int,
то вернуть строку 'Start and Step must be int!'.
"""
import itertools
import numpy as np


def pow3_start_inf_step(start: int, step: int):
    if type(start) != int or type(step) != int:
        return 'Start and Step must be int!'

    return (x ** 3 for x in itertools.count(start, step))


if __name__ == '__main__':
    pow3_gen = pow3_start_inf_step(2, 3)

    first_element = next(pow3_gen)
    second_element = next(pow3_gen)

    print(f'1: {first_element}')
    print(f'2: {second_element}')

    for n in range(3, 8):
        print(f'{n}: {next(pow3_gen)}')

    # ------------------

    next_element = next(pow3_gen)
    # x = next_element ** (1/3)   # с погрешностью
    x = int(np.cbrt(next_element))
    print(f"x={x} gen = {next_element}")
