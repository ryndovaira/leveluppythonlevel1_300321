"""
Функция triple_string_len.

Принимает строку my_str.
Вернуть эту строку в таком виде: "<my_str>, <my_str>? <my_str>! len=<len(my_str)> :)".

Если строка пустая, то вернуть None
"""


def triple_string_len(my_str):
    my_str_len = len(my_str)

    # способ 1:
    # if my_str_len == 0:
    #     return None
    # else:
    #     return f"{my_str}, {my_str}? {my_str}! len={my_str_len} :)"

    # способ 2:
    # if my_str_len > 0:
    #     return f"{my_str}, {my_str}? {my_str}! len={my_str_len} :)"

    # способ 3:
    if my_str_len:
        return f"{my_str}, {my_str}? {my_str}! len={my_str_len} :)"
