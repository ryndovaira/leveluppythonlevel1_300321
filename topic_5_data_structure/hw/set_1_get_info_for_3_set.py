"""
Функция get_info_for_3_set.

Принимает 3 аргумента: множества my_set_left, my_set_mid и my_set_right.

Возвращает dict с информацией:
{
'left == mid == right': True/False,
'left == mid': True/False,
'left == right': True/False,
'mid == right': True/False,

'left & mid': set(...), # intersection
'left & right': set(...),   # intersection
'mid & right': set(...),# intersection

'left <= mid': True/False, # issubset
'mid <= left': True/False, # issubset
'left <= right': True/False,   # issubset
'right <= left': True/False,   # issubset
'mid <= right': True/False,# issubset
'right <= mid': True/False # issubset
}

Если вместо множеств передано что-то другое, то возвращать строку 'Must be set!'.
"""