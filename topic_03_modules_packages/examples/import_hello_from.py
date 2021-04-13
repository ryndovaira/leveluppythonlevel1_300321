# Импортируем функцию hello из модуля hello
# from hello import hello, fun1
# from hello import my_global_var

# аналогично
from topic_03_modules_packages.examples.hello import hello, fun1, my_global_var, pi as my_pi
from topic_03_modules_packages.examples import hello as my_hello

# importing hello module

print(my_hello.hello("Olga"))  # Hello, world
print(fun1(1, 9))
print(my_global_var)
print(my_pi)
print(my_hello.pi)

# Добавить в область видимости несколько функций
from math import sqrt, pi

print(pi)  # 3.141592653589793
print(sqrt(9))  # 3.0

# Можно добавить все функции/переменные/классы... из модуля
from math import *

print(asin(1))  # 1.5707963267948966

# Импортирования функций и переменных под другим названием
from math import cos as cosine, acos as arccosine

print(arccosine(cosine(.9)))  # 0.9000000000000001
print(arccosine(cosine(1.)))  # 0.9999999999999999

import math

if __name__ == '__main__':
    # тут полезная работа
    print("I'm here!")

    help(math)
