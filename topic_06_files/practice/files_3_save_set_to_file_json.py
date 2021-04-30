"""
Функция save_set_to_file_json.

Принимает 2 аргумента:
    строка (название файла или полный путь к файлу),
    словарь JSON (для сохранения).

Сохраняет словарь (JSON) в файл.

Загрузить словарь JSON (прочитать файл),
проверить его на корректность.
"""

import json


def save_set_to_file_json(my_path, my_json):
    with open(my_path, 'w') as f:
        json.dump(my_json, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    my_dict = {
        "Маша": [
            1,
            2,
            3
        ],
        "ОЛОЛО": {
            "1": "one",
            "2": "two"
        },
        "set": [
            9.844,
            3.222
        ]
    }

    path = 'json_simple.json'

    save_set_to_file_json(path, my_dict)

    with open(path, 'r') as file:
        json_loaded = json.load(file)

    print(json_loaded)
