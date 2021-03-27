class A:
    def hi(self):
        print("A")


class B(A):
    def hi(self):
        print("B")


class C(A):
    def hi(self):
        print("C")


class D(B, C):
    # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
    # если  необходимо использовать метод конкретного родителя
    # нужно напрямую вызвать его по имени класса, передав self в качестве аргумента
    def call_hi_c(self):
        C.hi(self)


d = D()
# Method Resolution Order / MRO
d.hi()  # B
d.call_hi_c()  # C

# В Python3 для определения порядка используется алгоритм поиска в ширину,
# то есть сначала интерпретатор будет искать метод hi в классе B,
# если его там нету - в классе С, потом A.
# В Python второй версии используется алгоритм поиска в глубину,
# то есть в данном случае - сначала B, потом - А, потом С.

print(D.mro())
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
