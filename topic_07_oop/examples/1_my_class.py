# Синтаксис:
# class <Person>(<Persons>):
#   statements


class Person:
    # количество созданных людей
    count = 0   # поле класса
    
    # вызов функции print на класса
    print('Привет! Этот класс уже определен!')

    # Конструктор (фабрика, которая создаёт экземпляры)
    def __init__(self, n, a):
        # Поле (атрибут) экземпляра (с названием name)
        self.name = n
        self.age = a
        Person.count += 1

    # def method(self[, args]):
    #   statements
    def print_name(self):
        print(self.name)

    def __len__(self):
        return len(self.name) * 3


# class создаёт класс (объект-класс)
print(Person)
# <class '__main__.Person'>

# Создание экземпляра класса / инстанса
# инстанцирование (англ. instantiation)
vasya_22 = Person("Вася", 22)
print(vasya_22)
# <__main__.Person object at 0x7fc1ae739f50>

print(vasya_22.name)  # Вася

vasya_22.print_name()  # Вася

print(len(vasya_22))

print(Person.count)  # 1
print(vasya_22.count)  # 1

olya_66 = Person("Оля", 66)

olya_66.print_name()  # Оля

print(len(olya_66))

print(Person.count)  # 2
print(vasya_22.count)  # 2
print(olya_66.count)  # 2
