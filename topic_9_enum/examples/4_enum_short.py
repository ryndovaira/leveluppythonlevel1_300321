from enum import Enum, auto


# класс Animal - это перечисление
class Animal(Enum):
    # элементы перечисления, константы (не изменяются)
    # элементы имеют имена и значения
    # функция auto() автоматически присваивает элементу значение от 1 до N-1 с шагом 1
    cat = auto()  # 1
    dog = auto()  # 1 + 1 = 2
    frog = auto()  # 2 + 1 = 3
    duck = auto()  # 3 + 1 = 4


# эквивалентная более короткая запись
AnimalShort = Enum('Animal', "cat dog frog duck")

if __name__ == '__main__':
    print(Animal)
    for ae in Animal:
        print(ae, ae.value)

    print("-"*50)
    print(AnimalShort)
    for ase in AnimalShort:
        print(ase, ase.value)
