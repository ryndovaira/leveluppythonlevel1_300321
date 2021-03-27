# Синтаксис:
# class <ClassName>(<ClassNames>):
#   statements


class MyClass:
    count = 0   # поле класса
    print('Привет! Этот класс уже определен!')

    # Конструктор (фабрика, которая создаёт экземпляры)
    def __init__(self, n):
        # Поле (атрибут) экземпляра (с названием name)
        self.name = n
        MyClass.count += 1

    # def method(self[, args]):
    #   statements
    def print_name(self):
        print(self.name)

    def __len__(self):
        return len(self.name) * 3


# class создаёт класс (объект-класс)
print(MyClass)
# <class '__main__.MyClass'>

# Создание экземпляра класса
# инстанцирование (англ. instantiation)
instance = MyClass("MyObject")
print(instance)
# <__main__.MyClass object at 0x7fc1ae739f50>

print(instance.name)  # MyObject

instance.print_name()  # MyObject

print(len(instance))

print(MyClass.count)  # 1
print(instance.count)  # 1

instance2 = MyClass("MyObject2")

instance2.print_name()  # MyObject2

print(len(instance2))

print(MyClass.count)  # 2
print(instance.count)  # 2
print(instance2.count)  # 2
