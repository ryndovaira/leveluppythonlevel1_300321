"""
Функция count_even_num.

Принимает натуральное число (целое число > 0).
Верните количество четных цифр в этом числе.
Если число не целое (не int, а другой тип данных), то вернуть "Must be int!".
Если число меньше или равно 0, то вернуть "Must be > 0!".
"""


def count_even_num(num):
    if type(num) != int:
        return "Must be int!"
    # elif в данном контексте будет эквивалентно
    # elif num <= 0:
    if num <= 0:
        return "Must be > 0!"

    even_count = 0
    # способ 1:
    # num_str = str(num)
    # for char in num_str:
    #     if int(char) % 2 == 0:
    #         even_count += 1

    # способ 2:
    while num > 0:
        # tmp_num = num % 10
        # if tmp_num % 2 == 0:
        if num % 2 == 0:
            even_count += 1

        # num = num // 10
        num //= 10

    return even_count


if __name__ == '__main__':
    count_even_num(56326)
