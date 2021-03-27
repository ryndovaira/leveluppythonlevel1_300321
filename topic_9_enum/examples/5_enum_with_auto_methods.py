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

    def __gt__(self, other):
        return self.value > other.value

    def info(self):
        return f"Name: {self.name} | Value: {self.value}"


if __name__ == '__main__':
    print(Animal.cat.info())

    print(Animal.duck > Animal.dog)
    print(Animal.cat > Animal.dog)
