"""
Функция swap.

Принимает 2 аргумента (first_param, second_param) с некоторыми значениями.
Поменять местами значения этих переменных и
вывести на экран таким образом "first_param = 3 | second_param = True".
"""


def swap(first_param, second_param):
    # tmp = first_param
    # first_param = second_param
    # second_param = tmp

    first_param, second_param = second_param, first_param

    print(f"first_param = {first_param} | second_param = {second_param}")

    # без явного return
    # невидимо происходит это:
    # return None


if __name__ == '__main__':
    swap(5, "hi")

    result = swap(False, 8.76)
    print(result)

    a = 5
    b = True
    swap(a, b)
    print(f"a = {a} | b = {b}")

