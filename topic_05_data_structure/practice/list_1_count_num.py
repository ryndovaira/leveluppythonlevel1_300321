"""
Функция count_num.

Принимает 2 аргумента: список числами my_list и число num.

Возвращает количество num в списке my_list.

(Порядок проверки именно такой:)

Если вместо списка передано что-то другое, то возвращать строку 'First arg must be list!'.
Если вместо числа передано что-то другое, то возвращать строку 'Second arg must be int!'.
Если список пуст, то возвращать строку 'Empty list!'.
"""


def count_num(my_list: list, num: int):
    if type(my_list) != list:
        return 'First arg must be list!'
    if type(num) != int:
        return 'Second arg must be int!'
    if len(my_list) == 0:
        return 'Empty list!'

    return my_list.count(num)


if __name__ == '__main__':
    test_list_1 = [1, 3, None, 'lolol']
    my_num = 99
    result = count_num(test_list_1, my_num)
    print(result)
    print(f'result = {result}')

    # -------

    print('result2 =', count_num([5, 4, 3, 5, '88'], 5))

    # --------------------------

    print(['234', 'uuu', 'uuu', 65, None, 45].count('uuu'))
