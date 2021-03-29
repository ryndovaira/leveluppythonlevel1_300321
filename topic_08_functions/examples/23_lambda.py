# lambda умножает аргумент a на аргумент b и выводит результат
ab = lambda a, b: a * b
print('ab: ', ab(5, 6))  # 30

power_5 = lambda x: x ** 5
print('power_5: ', power_5(2))

print('(lambda x: x + 1)(2):', (lambda x: x + 1)(2))

full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print(full_name('guido', 'van rossum'))

ex1 = sorted([1, 2, 2, 3, 4, 5, 6], key=lambda x: -x)
print('ex1: ', ex1)  # [6, 5, 4, 3, 2, 2, 1]

high_ord_func = lambda x, func: x + func(x)
print('high_ord_func(2, lambda x: x * x): ', high_ord_func(2, lambda x: x * x))  # 6
print('high_ord_func(2, lambda x: x + 3): ', high_ord_func(2, lambda x: x + 3))  # 7

print('(lambda x, y, z: x + y + z)(1, 2, 3): ', (lambda x, y, z: x + y + z)(1, 2, 3))  # 6

print('(lambda x, y, z=3: x + y + z)(1, 2): ', (lambda x, y, z=3: x + y + z)(1, 2))  # 6

print('(lambda x, y, z=3: x + y + z)(1, y=2): ', (lambda x, y, z=3: x + y + z)(1, y=2))  # 6

print('(lambda *args: sum(args))(1, 2, 3): ', (lambda *args: sum(args))(1, 2, 3))  # 6

print('(lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3): ',
      (lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3))  # 6


# ----------------------------------------------------------------------------------------------------------------------
# Продвинутый уровень (для самостоятельно изучения по желанию):

print('(lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3): ',
      (lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3))  # 6

# Области видимости
mults_1 = [lambda x: x * i for i in range(5)]
print('mults_1: ', mults_1)
print(mults_1[4](2))  # 8
print(mults_1[0](2))  # 8

# Для захвата не переменной, а её значение можно использовать опциональные аргументы
mults_2 = [lambda x, i=i: x * i for i in range(5)]
print('mults_2: ', mults_2)
print(mults_2[4](2))  # 8
print(mults_2[0](2))  # 0
