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
