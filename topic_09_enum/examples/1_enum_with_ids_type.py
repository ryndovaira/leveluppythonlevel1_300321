from enum import Enum


# класс Colour - это перечисление
class Colour(Enum):
    # элементы перечисления, константы (не изменяются)
    # элементы имеют имена и значения
    # TODO: RGB
    red = 33
    blue = 66
    green = 11


if __name__ == '__main__':
    print(f"Colour.green = {Colour.green}")
    print(f"Colour.green.name = {Colour.green.name}")
    print(f"Colour.green.value = {Colour.green.value}")

    # тип элемента перечисления — это перечисление
    print(f"type(Colour.green) = {type(Colour.green)}")


