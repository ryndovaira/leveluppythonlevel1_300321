class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other: str):
        return str(other) + ' ' + self.name

    def __radd__(self, other: str):
        return self.__add__(other)
        # return str(other) + ' ' + self.name

    def __len__(self):
        return self.age

    def __str__(self):
        return f"{'*' * 50}\nName: {self.name}\nAge: {self.age}\n{'*' * 50}"


rex = Dog('Rex', 2)

print(f'Возраст собаки {rex.name} {rex.age} лет')

# __add__ и оператор (+)

# Вызов __add__ у Dog
print(rex + 'Inspector')
print(rex.__add__('Inspector'))  # эквивалентно
print(rex + 4)
# Inspector Rex

# Вызов __radd__ у str
print('Inspector' + rex)
print(rex.__radd__('Inspector'))  # эквивалентно

# Без использования __radd__:
# TypeError: can only concatenate str (not "Dog") to str

print(len(rex))

print(rex)
