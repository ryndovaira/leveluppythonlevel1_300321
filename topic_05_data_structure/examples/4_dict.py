print('\n--------------------------------------- Introduction --------------------------------------------------------')
# Создание пустого словаря
empty_1 = {}
empty_2 = dict()

# Синтаксис описания словаря: список пар ключ: значения в фигурных скобках через запятую
d = {1: 'one', 2: 'two', 3: 'three'}
print(d)  # {1: 'one', 2: 'two', 3: 'three'}

# Синтаксис добавления элемента
d[4] = 'four'
print(d)  # {1: 'one', 2: 'two', 3: 'three', 4: 'four'}

# Синтаксис обращения к значению по ключу
print(d[1])  # 'one'
# print(d[8])  # KeyError: 8

print(d.get(2, '2 не найдено'))
print(d.get(8, "8 не найдено"))

print('\n--------------------------------------- For -----------------------------------------------------------------')
my_dict = {1: 'one', 2: 'two', 3: 'three'}
for key, value in my_dict.items():
    print(f'key: {key} | value: {value}')

for key in my_dict.keys():
    print(f'key: {key}')

for value in my_dict.values():
    print(f'value: {value}')

print('\n--------------------------------------- Details -------------------------------------------------------------')
dict1 = {1: 'one', 2: 'two', 3: 'three'}
dict2 = {'rrr': '3-5-33', 'tre': '083-7363-33', 3: 'три'}

dict3 = {}
dict3.update(dict1)
print(dict3)  # {1: 'one', 2: 'two', 3: 'three'}
dict3.update(dict2)  # {1: 'one', 2: 'two', 3: 'три', 'rrr': '3-5-33', 'tre': '083-7363-33'}
print(dict3)

del dict3[1]
print(dict3)
