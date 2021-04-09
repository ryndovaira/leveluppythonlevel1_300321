"""
Функция check_numbers_by_5.

Принимает 3 числа.
Если ровно два из них меньше 5, то вернуть True, иначе вернуть False.
"""


def check_numbers_by_5(n1, n2, n3):
    # первый вариант:
    # закомментировать/раскомментировать команда ctr+/
    # # if n1 < 5 and n2 < 5 and n3 >= 5:
    # if n1 < 5 <= n3 and n2 < 5:
    #     return True
    # # elif n1 >= 5 and n2 < 5 and n3 < 5:
    # elif n1 >= 5 > n2 and n3 < 5:
    #     return True
    # # elif n1 < 5 and n2 >= 5 and n3 < 5:
    # elif n1 < 5 and n2 >= 5 > n3:
    #     return True
    # else:
    #     return False

    # альтернативный вариант 1:
    # print("Example:",
    #       (n1 < 5 and n2 < 5 and n3 >= 5) or
    #       (n1 >= 5 and n2 < 5 and n3 < 5))
    #
    # if (n1 < 5 and n2 < 5 and n3 >= 5) or \
    #         (n1 >= 5 and n2 < 5 and n3 < 5) or \
    #         (n1 < 5 and n2 >= 5 and n3 < 5):
    #     return True
    # else:
    #     return False

    # альтернативный вариант 2:
    return (n1 < 5 and n2 < 5 and n3 >= 5) or \
           (n1 >= 5 and n2 < 5 and n3 < 5) or \
           (n1 < 5 and n2 >= 5 and n3 < 5)


if __name__ == "__main__":
    print("Hello!")

    print("dskdjf",
          444,
          "38383",
          33332, sep="*")

    print(check_numbers_by_5(5, 4, 1))
