"""
Функция check_equal.

Принимает 3 числа.
Вернуть True, если среди них есть одинаковые, иначе False.
"""


def check_equal(num1, num2, num3):
    # if not (num1 == num2 or num1 == num3 or num2 == num3):
    #     return True
    # else:
    #     return False

    # return not (num1 == num2 or num1 == num3 or num2 == num3)
    return num1 == num2 or num1 == num3 or num2 == num3


if __name__ == '__main__':
    # check_equal(1, 3, 1)

    n1 = input("Введите 1 число: ")
    n2 = input("Введите 2 число: ")
    n3 = input("Введите 3 число: ")

    result = check_equal(n1, n2, n3)

    print(f"{n1} & {n2} & {n3} => {result}")
