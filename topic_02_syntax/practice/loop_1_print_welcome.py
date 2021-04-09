"""
Функция print_welcome.

Принимает число n.
Выведите на экран n раз фразу "You are welcome!".
Пример: n=3, тогда в результате "You are welcome!You are welcome!You are welcome!"
"""


def print_welcome(n):
    my_string = "You are welcome!" * n
    print(my_string)


if __name__ == '__main__':
    print_welcome(0)    # при 0 множителе будет пустая строка
    print_welcome(1)
    print_welcome(3)
    print_welcome(-2)   # при отрицательных множителях будет пустая строка
