"""
Функция magic_parts.

Принимает 1 аргумент: список my_list.

Возвращает список, который состоит из
[первые 2 элемента my_list]
+ [последний элемент my_list]
+ [количество элементов в списке my_list].

Пример: входной список [1, 2, 'aa', 'mm'], результат [1, 2, 'mm', 4].

(Порядок проверки именно такой:)

Если вместо списка передано что-то другое, то возвращать строку 'Must be list!'.
Если список пуст, то возвращать строку 'Empty list!'.
"""


def magic_parts(my_list: list):
    if type(my_list) != list:
        return 'Must be list!'
    elif len(my_list) == 0:
        return 'Empty list!'

    result_list = []

    # first_el = my_list[0]
    # так будет ошибка, если в my_list только один элемент при обращении по индексу 1
    # second_el = my_list[1]

    first_second_el = my_list[:2]
    last_el = my_list[-1]
    len_el = len(my_list)

    result_list.extend(first_second_el)     # так как добавляем элементы из списка
    result_list.append(last_el)             # так как добавляем один элемент
    result_list.append(len_el)

    return result_list


if __name__ == '__main__':
    magic_parts([1])
    magic_parts([1, 5])
    magic_parts([1, 5, 3])
