print('\n--------------------------------------- Introduction --------------------------------------------------------')
# Синтаксис описания простейшего кортежа: список значений в круглых скобках через запятую
ex1 = (1, 2, 3)
print(ex1)  # (1, 2, 3)

# del ex1[1]      # 'tuple' object doesn't support item deletion
# ex1[1] = 777    # 'tuple' object does not support item assignment

# Скобки можно опустить
ex2 = 1, 2, 3
print(ex2)  # (1, 2, 3)

# Для определения кортежа единичной длины указывается запятая без элемента
ex3 = (1,)
print(ex3)  # (1,)

# Для определения кортежа нулевой длины можно использовать пару круглых скобок
ex4 = ()
print(ex4)  # ()

# tuple packing (упаковка)
x = ("LevelUp", 20, "teacher")  # можно без ()
print(f'x = {x}')

# tuple unpacking (распаковка)
(company, emp, profile) = x  # можно без ()
print(f'company = {company}\nemp = {emp}\nteacher = {profile}')

# ValueError: too many values to unpack (expected 2)
# (company, emp) = x

# в переменную со * сохранятся остальные значения
(company, *emp_profile) = x

# Кортежи при написании перестановкой значений
a = 1
b = 2
print(f"a = {a}; b = {b}")  # a = 1; b = 2
a, b = b, a  # (a, b) = (b, a)
print(f"a = {a}; b = {b}")  # a = 2; b = 1


# ------------------------------------------

def fun_return_multi_result():
    # return (123, 'hi', 34.5)      # tuple
    return 123, 'hi', 34.5  # tuple


res = fun_return_multi_result()

a, b, c = fun_return_multi_result()

var1, _, var3 = fun_return_multi_result()


# -------------------------------------------

def my_strange_fun(n):
    if n == 0:
        return 'Zero',  # tuple из 1 элементов
    elif n > 0:
        return 'Big number', n  # tuple из 2 элементов
    elif n < 0:
        return 'Small number', -1, None  # tuple из 3 элементов


my_res0 = my_strange_fun(0)
my_res4 = my_strange_fun(4)
my_res_3 = my_strange_fun(-3)

if len(my_res4) == 2:
    print('It is a positive number')

# ----------------------------------------------

# list  - это итерируемый тип и поэтому его можно использовать в for
for element in (2, None, 'opopo', 7.77):
    print(element)
