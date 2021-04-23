"""
Функция get_name_by_number.

Принимает 2 аргумента:
    словарь содержащий {имя: [телефон1, телефон2, ...], ...},
    номер телефона (строка) для поиска в словаре.

Возвращает имя владельцев телефона (список), если такой номер есть в словаре,
если нет, то "Can't find phone: {phone}".

(Порядок проверки именно такой:)

Если вместо словаря передано что-то другое, то возвращать строку "Dictionary must be dict!".
Если вместо строки для поиска передано что-то другое, то возвращать строку "Phone number must be str!".

Если словарь пустой, то возвращать строку "Dictionary is empty!".
Если строка для поиска пустая, то возвращать строку "Phone number is empty!".
"""


def get_name_by_number(my_dict: dict, tel: str):
    if type(my_dict) != dict:
        return "Dictionary must be dict!"
    elif type(tel) != str:
        return "Phone number must be str!"
    elif len(my_dict) == 0:
        return "Dictionary is empty!"
    elif len(tel) == 0:
        return "Phone number is empty!"
    else:
        names = []
        for name, tels in my_dict.items():
            if tel in tels:
                names.append(name)

        return names if len(names) > 0 else f"Can't find phone: {tel}"


if __name__ == '__main__':
    test_dict = {"ira": ["1-2-3"],
                 "ivan": ["33-44-55", "99-3-1"],
                 "olga": ["99-3-1"]}

    get_name_by_number(test_dict, "99-3-1")
