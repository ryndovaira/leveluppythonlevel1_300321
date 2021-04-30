"""
Функция save_set_to_file_pickle.

Принимает 2 аргумента:
    строка (название файла или полный путь к файлу),
    множество (для сохранения).

Сохраняет множество в файл.

Загрузить множество (прочитать файл) и проверить его на корректность и тип.
"""

import pickle


def save_set_to_file_pickle(my_path, my_set):
    with open(my_path, 'wb') as pickle_file:
        pickle.dump(my_set, pickle_file)


if __name__ == '__main__':
    ex_set = {3, 4, 5, 6, 7}
    path = 'set.pkl'

    save_set_to_file_pickle(path, ex_set)

    with open(path, 'rb') as f:
        set_loaded = pickle.load(f)

    # проверка
    print(f'type: {type(set_loaded)}')
    print(f'equal: {ex_set == set_loaded}')
