"""
Функция count_num.

Принимает 2 аргумента: список числами my_list и число num.

Возвращает количество num в списке my_list.

(Порядок проверки именно такой:)

Если вместо списка передано что-то другое, то возвращать строку 'First arg must be list!'.
Если вместо числа передано что-то другое, то возвращать строку 'Second arg must be int!'.
Если список пуст, то возвращать строку 'Empty list!'.
"""


def count_num(my_list, num):
    if type(my_list) != list:
        return 'First arg must be list!'
    elif type(num) != int:
        return 'Second arg must be int!'
    elif len(my_list) == 0:
        return 'Empty list!'

    return my_list.count(num)
