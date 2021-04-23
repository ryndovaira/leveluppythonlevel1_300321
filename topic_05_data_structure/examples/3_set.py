print('\n--------------------------------------- Introduction --------------------------------------------------------')
# Синтаксис описания множества: список значений в фигурных скобках через запятую
ex1 = {1, 2, 3}
print(ex1)  # {1, 2, 3}

# Для определения пустого множества необходимо явно вызвать конструктор
# Это вызвано тем, что {} описывает пустой словарь
ex2 = set()
print(ex2)  # set()
print(ex2 or '{}')  # {}

print('\n--------------------------------------- Details -------------------------------------------------------------')
set_1 = {1, 2, 3, 4, 4}  # Останутся только уникальные значения!
set_2 = {4, 5, 6, 7}
set_3 = {3, 4}
print(f'{set_1} | {set_2} | {set_3}')

# истина, если set и other не имеют общих элементов
print('set_1.isdisjoint(set_2) => ', set_1.isdisjoint(set_2))

# все элементы left принадлежат right
print('set_1.issubset(set_2) => ', set_1.issubset(set_2))
print('set_3.issubset(set_2) => ', set_3.issubset(set_2))

# все элементы right принадлежат left
print('set_1.issuperset(set_2) => ', set_1.issuperset(set_2))
print('set_1.issuperset(set_3) => ', set_1.issuperset(set_3))

# пересечение
print('set_1.intersection(set_2) => ', set_1.intersection(set_2))
print('set_1.intersection(set_3) => ', set_1.intersection(set_3))

# объединение нескольких множеств
print('set_1.union(set_3) => ', set_1.union(set_3))
print('set_1.union(set_2, set_3) => ', set_1.union(set_2, set_3))

# можно передавать итерируемые типы (которые подходят для цикла for)
print(set_1.union(set_2, (3, 5, 3)))
print(set_1.union(set_2, [3, 5, 3]))
# print(set_1.union(set_2, 9))
print(set_1.union(set_2, range(9, 15, 2)))
print(set_1.union(set_2, "kdjfsdh34jh"))

# множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих
print('set_1.difference(set_2, set_3) => ', set_1.difference(set_2, set_3))

print(set_1 == set_2)

print(set_1 > set_2)  # TODO

# -----------------------

# list  - это итерируемый тип и поэтому его можно использовать в for
for element in {2, None, 'opopo', 7.77}:
    print(element)
