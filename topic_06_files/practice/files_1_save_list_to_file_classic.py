"""
Функция save_list_to_file_classic.

Принимает 2 аргумента:
строка (название файла или полный путь к файлу),
список (для сохранения).

Сохраняет список в файл. Проверить, что записалось в файл (прочитать файл).
"""


def save_list_to_file_classic(path, my_list):
    with open(path, 'w') as my_file:
        # TypeError: write() argument must be str, not list
        my_file.write(str(my_list))


if __name__ == '__main__':
    my_path = 'my_list.txt'
    save_list_to_file_classic(my_path, [1, 2, 3, 4])

    with open(my_path, 'r') as f:
        my_list_str = f.read()
        print(my_list_str)
