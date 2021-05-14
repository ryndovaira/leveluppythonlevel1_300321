from enum import Enum


# класс Notes - это перечисление
class Notes(Enum):
    # элементы перечисления, константы (не изменяются)
    # элементы имеют имена и значения
    emergency_tels = {112, 111, 222}
    friend_tels = [123, 345, 666, 777]
    worker_names = ('Anton', 'Kate')

    # worker_names = ('Anton', 'Kate')    # TypeError: Attempted to reuse key: 'worker_names'

    friends_names = ('Anton', 'Kate')  # будет пропущено


if __name__ == '__main__':
    for element in Notes:
        print(f"{element}: {element.value}")

    print(Notes.friends_names, Notes.friends_names.name, Notes.friends_names.value)
