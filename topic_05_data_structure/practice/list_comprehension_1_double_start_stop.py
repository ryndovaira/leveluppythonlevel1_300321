"""
Функция double_start_stop.

Принимает 2 аргумента: числа start, stop.

Возвращает список состоящий из удвоенных значений
от start до stop (не включая).

Пример: start=3, stop=6, результат [6, 8, 10].

Если start или stop не являются int,
то вернуть строку 'Start and Stop must be int!'.
"""


def double_start_stop(start: int, stop: int):
    if type(start) != int or type(stop) != int:
        return 'Start and Stop must be int!'

    return [num * 2 for num in range(start, stop)]
