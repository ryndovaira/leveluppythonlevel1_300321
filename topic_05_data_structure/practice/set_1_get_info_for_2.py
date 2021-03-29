"""
Функция get_info_for_2.

Принимает 2 аргумента: множества left и right.

Возвращает dict с информацией:
{
'left == right': True/False,# равенство

'left & right': set(...),   # intersection

'left <= right': True/False,   # issubset
'right <= left': True/False,   # issubset
}

Если вместо множеств передано что-то другое, то возвращать строку 'Must be set!'.
"""