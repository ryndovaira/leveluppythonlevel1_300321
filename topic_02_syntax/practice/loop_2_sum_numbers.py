"""
Функция sum_numbers.

Принимает строку string содержащую целое число больше или равное 0.
Пример: '123', '00', '0603', '0054310003323566767'.
Вернуть сумму этих чисел.
Пример: string='0603', result=9 (0+6+0+3).

Строка не должна содержать пробелов или любых других символов,
то есть должна корректно конвертироваться в int.
Подсказка: isdigit()
Если строка не соответствует этим требованиям, то вернуть None.
Пример (с ошибкой): '765eew', '5 57 767', '$ewe23', '664.232', ''.
"""


def sum_numbers(string):
    # if not string:
    #     return None

    if not string.isdigit():
        return None

    my_sum = 0
    for my_symbol in string:
        # if not my_symbol.isdigit():
        #     return None
        my_sum += int(my_symbol)

    return my_sum


if __name__ == '__main__':
    print(sum_numbers("4*6"))

    print("0603".isdigit())
