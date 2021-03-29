# Импортируем функцию hello из модуля hello
from hello import hello
# importing hello module

print(hello())      # Hello, world

# Добавить в область видимости несколько функций
from math import sqrt, pi
print(pi)   # 3.141592653589793

# Можно добавить все функции из модуля
from math import *
print(asin(1))      # 1.5707963267948966

# Импортирования функций и переменных под другим названием
from math import cos as cosine, acos as arccosine
print(arccosine(cosine(.9)))    # 0.9000000000000001
print(arccosine(cosine(1.)))    # 0.9999999999999999

