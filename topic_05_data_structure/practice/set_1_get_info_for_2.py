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


def get_info_for_2(left: set, right: set):
    if type(left) != set or type(right) != set:
        return 'Must be set!'

    return {'left == right': left == right,  # равенство
            'left & right': left.intersection(right),  # intersection
            'left <= right': left.issubset(right),  # issubset
            'right <= left': right.issubset(left)}  # issubset
