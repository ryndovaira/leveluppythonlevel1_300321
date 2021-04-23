"""
Функция len_first.

Принимает 1 аргумент: кортеж my_tuple.

Возвращает кортеж состоящий из длины кортежа и первого элемента кортежа.

Пример: ('55', 'aa', 66), результат (3, '55').

(Порядок проверки именно такой:)

Если вместо tuple передано что-то другое, то возвращать строку 'Must be tuple!'.
Если tuple пуст, то возвращать строку 'Empty tuple!'.
"""


def len_first(my_tuple):
    if type(my_tuple) != tuple:
        return 'Must be tuple!'
    if len(my_tuple) == 0:
        return 'Empty tuple!'

    return len(my_tuple), my_tuple[0]


if __name__ == '__main__':
    res = len_first((888,))
    print(res)

    l, f = len_first((11, 2, 3))
    print(l, f)
