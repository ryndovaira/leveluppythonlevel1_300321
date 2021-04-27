# Генератор нельзя писать без скобок — это синтаксическая ошибка
import itertools

gen_exp = (f'{key}: {value}'
           for key, value in zip(range(100), 'abcdefghijklmno'))
print(list(gen_exp))  # ['0: a', '1: b', '2: c', '3: d', '4: e', '5: f', '6: g', ...]
# Нельзя распечатать элементы функцией print()
print(gen_exp)  # <generator object <genexpr> at 0x7f3ad1f92750>

my_list = [-2, -1, 0, 1, 2, 3, 4, 5]
my_gen = (i for i in my_list)    # выражение-генератор
print(next(my_gen))     # -2 - получаем очередной элемент генератора
print(next(my_gen))     # -1 - получаем очередной элемент генератора

# my_sum = sum((i for i in list_a))  # так тоже можно
print(sum(my_gen))   # 15
# после прохождения по выражению-генератору оно остается пустым!
print(sum(my_gen))   # 0
# print(next(my_gen))   # StopIteration

# Выражение-генератор может быть бесконечным
inf_gen = (x for x in itertools.count())  # бесконечный генератор от 0 to бесконечности!
# list(inf_gen) Зависание!!!

# dict_gen = (x: x**2 for x in list_a)      # SyntaxError: invalid syntax
dict_gen = ((x, x ** 2) for x in my_list)    # Корректный вариант генератора-выражения для словаря
print(dict(dict_gen))   # {-2: 4, -1: 1, 0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# dict_a = dict(x: x**2 for x in list_a)    # SyntaxError: invalid syntax
my_dict = dict((x, x ** 2) for x in my_list)  # Корректный вариант синтаксиса
print(my_dict)      # {-2: 4, -1: 1, 0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
