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


if __name__ == '__main__':
    # элементы перечисления можно использовать их в словарях (dict) и множествах (set)
    my_animals_dict = dict()
    my_animals_dict[Animal.cat] = 'Kesha'
    my_animals_dict[Animal.dog] = 'Bulba'
    print(my_animals_dict)
    # {<Animal.cat: 1>: 'Kesha', <Animal.dog: 2>: 'Bulba'}

    my_animals_set = set()
    my_animals_set.add(Animal.dog)
    my_animals_set.add(Animal.cat)
    my_animals_set.add(Animal.dog)
    print(my_animals_set)
    # {<Animal.dog: 2>, <Animal.cat: 1>}
