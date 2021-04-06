"""
Функция season.

Принимает 1 аргумент — номер месяца (от 1 до 12).
Возвращает время года, которому этот месяц принадлежит
('Winter', 'Spring', 'Summer' или 'Fall').
Если номер месяца не входит в диапазон от 1 до 12, то вернуть None.
"""


def season(my_num):
    # if my_num == 12 or my_num == 1 or my_num == 2:
    if my_num in (12, 1, 2):
        return 'Winter'
    elif my_num == 3 or my_num == 4 or my_num == 5:
        return 'Spring'
    # elif my_num == 6 or my_num == 7 or my_num == 8:
    elif my_num >= 6 and my_num <= 8:
        return 'Summer'
    # elif my_num == 9 or my_num == 10 or my_num == 11:
    elif 9 <= my_num <= 11:
        return 'Fall'


if __name__ == '__main__':
    result = season(9.5)
    print(result)
    print(season(99))
