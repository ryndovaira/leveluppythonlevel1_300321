"""
Функция zip_common.

Принимает 3 аргумента: список, строку и кортеж.

Возвращает список (list) с тройками значений из каждого аргумента.
ВНИМАНИЕ: для строки один элемент = один символ

(Порядок проверки именно такой:)

Если вместо list передано что-то другое, то возвращать строку 'First arg must be list!'.
Если вместо str передано что-то другое, то возвращать строку 'Second arg must be str!'.
Если вместо tuple передано что-то другое, то возвращать строку 'Third arg must be tuple!'.

Если list пуст, то возвращать строку 'Empty list!'.
Если str пуст, то возвращать строку 'Empty str!'.
Если tuple пуст, то возвращать строку 'Empty tuple!'.

Если list, str и tuple различного размера, обрезаем до минимального (стандартный zip).
"""


def zip_common(my_list, my_str, my_tuple):
    if type(my_list) != list:
        return 'First arg must be list!'
    if type(my_str) != str:
        return 'Second arg must be str!'
    if type(my_tuple) != tuple:
        return 'Third arg must be tuple!'

    if len(my_list) == 0:
        return 'Empty list!'
    if len(my_str) == 0:
        return 'Empty str!'
    if len(my_tuple) == 0:
        return 'Empty tuple!'

    return list(zip(my_list, my_str, my_tuple))
