"""
Функция print_3th_symbols.

Принимает строку.
Вывести третий, шестой, девятый и так далее символы.
"""


def print_3th_symbols(my_str):
    print(my_str[2::3])


if __name__ == '__main__':
    print_3th_symbols("0123456789")
