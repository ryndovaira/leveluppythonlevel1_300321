# def имя_функции(аргументы):
def arithmetic_sum(n):
    """
    Получить сумму чисел [0, n)
    :param n: целое число
    :return: сумма чисел [0, n)
    """

    acc = 0
    for i in range(n):
        acc += i

    # return может и не быть
    return acc


if __name__ == '__main__':
    print('sum(3) = ', arithmetic_sum(3))
    # sum(3) =  3

    print('sum(10) = ', arithmetic_sum(10))
    # sum(10) =  45

    print('sum(166) = ', arithmetic_sum(166))
    # sum(166) =  13695

    help(arithmetic_sum)

    # exit(33)
