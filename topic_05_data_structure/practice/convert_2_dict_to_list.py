"""
Функция dict_to_list.

Принимает 1 аргумент: словарь.

Возвращает список: [
    список (list) ключей,
    список (list) значений,
    количество элементов в списке ключей в степени 3,
    количество уникальных элементов в списке значений,
    хотя бы один ключ равен одному из значений (True | False).
]

Если вместо словаря передано что-то другое, то возвращать строку 'Must be dict!'.

Если dict пуст, то возвращать [[], [], 0, 0, False].
"""


def dict_to_list(my_dict: dict):
    if type(my_dict) != dict:
        return 'Must be dict!'
    elif not my_dict:
        return [[], [], 0, 0, False]

    keys_list = list(my_dict.keys())
    values_list = list(my_dict.values())
    len_keys_pow_3 = len(keys_list) ** 3
    len_unique_values = len(set(values_list))


    # Способ 1
    # key_equal_val = False
    # for k in my_dict.keys():
    #     for v in my_dict.values():
    #         if k == v:
    #             key_equal_val = True
    #             break
    #     if key_equal_val:
    #         break

    # Способ 2
    # key_equal_val = False
    # for k in my_dict.keys():
    #     # key_equal_val = k in values_list
    #     # if key_equal_val:
    #     #     break
    #     if k in values_list:
    #         key_equal_val = True
    #         break

    # Способ 3
    key_equal_val = True
    for k in my_dict.keys():
        if k in values_list:
            break
    else:
        # перейдем сюда только, если не сработал break
        key_equal_val = False

    return [keys_list, values_list, len_keys_pow_3, len_unique_values, key_equal_val]


if __name__ == '__main__':
    dict_to_list({1: 3, 2: 3, 3: 1, 4: 7})
