"""
Функция list_to_dict.

Принимает 2 аргумента: список и значение для поиска.

Возвращает словарь (из входного списка), в котором
ключ = значение из списка,
значение = (
индекс (последний, если есть несколько одинаковых значений) этого элемента в списке,
равно ли значение из списка искомому значению (True | False),
количество элементов в словаре.
)

Если список пуст, то возвращать пустой словарь.

Если вместо списка передано что-то другое, то возвращать строку 'First arg must be list!'.

ВНИМАНИЕ: количество элементов в словаре не всегда равно количеству элементов в списке!

ВНИМАНИЕ: при повторяющихся ключах в dict записывается значение последнего добавленного ключа.

ВНИМАНИЕ: нумерация индексов начинается с 0!
"""