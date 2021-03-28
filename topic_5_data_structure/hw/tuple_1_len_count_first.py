"""
Функция len_count_first.

Принимает 2 аргумента: кортеж my_tuple и строку word.

Возвращает кортеж состоящий из
длины кортежа,
количества word в кортеже my_tuple,
первого элемента кортежа.

Пример:
my_tuple=('55', 'aa', '66')
word = '66'
результат (3, 1, '55').

Если вместо tuple передано что-то другое, то возвращать строку 'First arg must be tuple!'.
Если вместо строки передано что-то другое, то возвращать строку 'Second arg must be str!'.
Если tuple пуст, то возвращать строку 'Empty tuple!'.
"""