"""
Функция print_diff_count.

Принимает две строки.

Вывести большую по длине строку столько раз,
насколько символов отличаются строки.

Если строки одинаковой длины, то вывести строку "Equal!".
"""


def print_diff_count(s1, s2):
    diff = len(s1) - len(s2)

    if diff == 0:
        print("Equal!")
    elif diff > 0:
        print(s1 * diff)
    else:
        print(s2 * -diff)
        # print(s2 * abs(diff))


if __name__ == '__main__':
    print_diff_count("123", "123456")
