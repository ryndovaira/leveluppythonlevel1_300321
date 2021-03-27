from enum import Enum, auto


# класс Animal - это перечисление
class Animal(Enum):
    # элементы перечисления, константы (не изменяются)
    # элементы имеют имена и значения
    # функция auto() автоматически присваивает элементу значение от 1 до N-1 с шагом 1
    cat = auto()    # 1
    dog = auto()    # 1 + 1 = 2
    frog = auto()   # 2 + 1 = 3
    duck = auto()   # 3 + 1 = 4


if __name__ == '__main__':
    # перечисления — это итерируемые объекты, т.е. все элементы можно перебрать в цикле
    for element in Animal:
        print(element)
        print(f"name = {element.name}")
        print(f"value = {element.value}\n")

