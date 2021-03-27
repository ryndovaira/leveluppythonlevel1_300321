class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        return str(other) + ' ' + self.name

    def __radd__(self, other):
        return str(other) + ' ' + self.name

    def __len__(self):
        return self.age

    def __str__(self):
        return f"{'*' * 50}\nName: {self.name}\nAge: {self.age}\n{'*' * 50}"


dog = Dog('Rex', 2)

print(f'Возраст собаки {dog.name} {dog.age} лет')

# __add__ и оператор (+)

# Вызов __add__ у Dog
print(dog + 'Inspector')
print(dog.__add__('Super'))  # эквивалентно
print(dog + 4)
# Inspector Rex

# Вызов __radd__ у str
print('Inspector' + dog)
print(dog.__radd__('Super'))  # эквивалентно

# Без использования __radd__:
# TypeError: can only concatenate str (not "Dog") to str

print(len(dog))

print(dog)
