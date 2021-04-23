"""
Функция get_numbers_by_name.

Принимает 2 аргумента:
    словарь содержащий {имя: [телефон1, телефон2], ...},
    слово (имя) для поиска в словаре.

(Порядок проверки именно такой:)

Если вместо словаря передано что-то другое, то возвращать строку "Dictionary must be dict!".
Если вместо строки для поиска передано что-то другое, то возвращать строку "Name must be str!".

Если словарь пустой, то возвращать строку "Dictionary is empty!".
Если строка для поиска пустая, то возвращать строку "Name is empty!".

Вернуть все телефоны по имени (list), если такое имя есть в словаре,
если нет, то "Can't find name: {name}".
"""


def get_numbers_by_name(my_dict: dict, word: str):
    if type(my_dict) != dict:
        return "Dictionary must be dict!"
    elif type(word) != str:
        return "Name must be str!"
    elif len(my_dict) == 0:
        return "Dictionary is empty!"
    elif len(word) == 0:
        return "Name is empty!"
    else:
        return my_dict.get(word, f"Can't find name: {word}")


if __name__ == '__main__':
    test_dict = {"ira": ["1-2-3"],
                 "ivan": ["33-44-55", "99-3-1"]}

    print(get_numbers_by_name(test_dict, 'ira'))
    print(get_numbers_by_name(test_dict, 'olga'))

    # проверить, что такой ключ существует
    print('ivan' in test_dict.keys())
