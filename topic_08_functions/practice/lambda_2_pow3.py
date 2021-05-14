"""
lambda возводит в 3ю степень переданный аргумент возвращает результат
"""


def fun(x):
    return x ** 3


print(fun(2))

# еще одно название для функции fun
alias_fun = fun

# эквивалентно print(fun(2))
print(alias_fun(2))

lam = lambda x: x ** 3

print(lam(2))

alias_lam = lam

print(alias_lam(2))
