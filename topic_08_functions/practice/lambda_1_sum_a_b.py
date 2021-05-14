"""
lambda складывает аргументы a и b и выводит результат
"""


def lam1(a, b):
    return a + b


print(lam1(3, 6))

print((lambda a, b: a + b)(3, 6))

(lambda a, b: print(a + b))(3, 6)

(lambda a, b: print(str(a)
                    + str(b)))(3, 6)
