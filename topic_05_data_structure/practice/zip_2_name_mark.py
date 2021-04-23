"""
Функция zip_name_mark.

Принимает 2 аргумента: список с именами и список с баллами.

Возвращает список (list) с парами значений из каждого аргумента, если один список больше другого,
то заполнить недостающие элементы строкой "!!!".

Подсказка: zip_longest.

(Порядок проверки именно такой:)

Если вместо списков передано что-то другое или список (хотя бы один) пуст,
то возвращать строку 'Both args must be list and not empty!'.

Если в списке с именами есть элементы НЕ str, то возвращать строку 'Names must be str!'

Если в списке с оценками есть элементы НЕ int (0 <= mark <= 100),
то возвращать строку 'Marks must be int (0 to 100)!'
"""
from itertools import zip_longest


def zip_name_mark(names, marks):
    if type(names) != list or type(marks) != list or len(names) == 0 or len(marks) == 0:
        return 'Both args must be list and not empty!'

    for n in names:
        if type(n) != str:
            return 'Names must be str!'

    for m in marks:
        # if type(m) != int or m > 100 or m < 0:
        if type(m) != int or not (0 <= m <= 100):
            return 'Marks must be int (0 to 100)!'

    return list(zip_longest(names, marks, fillvalue='!!!'))
