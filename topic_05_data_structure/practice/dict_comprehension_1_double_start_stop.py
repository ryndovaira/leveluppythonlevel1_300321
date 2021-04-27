"""
Функция double_start_stop.

Принимает 2 аргумента: числа start, stop.

Возвращает словарь, в котором
ключ - это значение от start до stop (не включая),
значение - удвоенных значение ключа.

Пример: start=3, stop=6, результат {3: 6, 4: 8, 5: 10}.

Если start или stop не являются int,
то вернуть строку 'Start and Stop must be int!'.
"""


def double_start_stop(start: int, stop: int):
    if type(start) != int or type(stop) != int:
        return 'Start and Stop must be int!'

    return {n: n * 2 for n in range(start, stop)}
