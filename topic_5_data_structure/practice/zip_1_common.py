"""
Функция zip_common.

Принимает 3 аргумента: список, строку и кортеж.

Возвращает список (list) с тройками значений из каждого аргумента.
ВНИМАНИЕ: для строки один элемент = один символ

Если вместо list передано что-то другое, то возвращать строку 'First arg must be list!'.
Если вместо str передано что-то другое, то возвращать строку 'Second arg must be str!'.
Если вместо tuple передано что-то другое, то возвращать строку 'Third arg must be tuple!'.

Если list пуст, то возвращать строку 'Empty list!'.
Если str пуст, то возвращать строку 'Empty str!'.
Если tuple пуст, то возвращать строку 'Empty tuple!'.

Если list, str и tuple различного размера, обрезаем до минимального (стандартный zip).
"""