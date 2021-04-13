# Импортируем функцию hello из модуля hello
# import hello
# аналогично
from topic_03_modules_packages.examples import hello

# importing hello module

print(hello)
# <module 'hello' from '/media/ira/.../Examples_L5/hello.py'>
type(hello)

print(hello.__file__)
# /media/ira/.../Examples_L5/hello.py

print(hello.__name__)
# hello

print(hello.hello('Ira'))

print(hello.fun1(4, 5))

print(hello.my_global_var)

