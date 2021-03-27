class Chair:
    # допустим у всех стульев одинаковый производитель
    company = 'original_name'  # поле класса

    def __init__(self, colour):
        # каждый стул имеет свой цвет
        self.colour = colour  # поле экземпляра

    def change_company(self, new_company_name):
        # инициализация (создание и присвоение значения) поля экземпляра
        # (с таким же именем как и поле класса)
        # поле экземпляра - скорее всего логическая ошибка
        self.company = new_company_name + "_obj"

        # изменение значения поля класса
        # поле класса - вероятно, верная логика
        self.__class__.company = new_company_name + "_cls"


def print_info(my_obj):
    print(f"\n{'-' * 50}\n{my_obj}.__dict__:")
    for param_key, param_val in my_obj.__dict__.items():
        print(f"{param_key}: {param_val}")
    print(f"{'-' * 50}")


chair_1 = Chair(1)

print_info(Chair)

print_info(chair_1)

chair_1.change_company('new_name')

print_info(Chair)

print_info(chair_1)


print(f"\n\n{'*' * 50}\n")

print("welcome".upper())  # метод экземпляра класса

print(dict.fromkeys('AEIOU'))  # метод класса dict
