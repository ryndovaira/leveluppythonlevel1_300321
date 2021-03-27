class Chair:
    # поле класса
    # рост человека по умолчанию
    default_human_height = 1.7

    def __init__(self, human_height=default_human_height):
        # поле экземпляра
        # высота стула изначально не заполняется
        self._chair_height = None

        # поле экземпляра
        # рост человека
        self._human_height = human_height

    def get_chair_height(self):
        if self._chair_height is None:
            # допустим, что это высота стула по умолчанию
            return 1.5
        else:
            # если рост человека задан, то
            if self._human_height is not None:
                # вычисляем высоту нужного стула по выдуманной формуле
                return self._chair_height * 0.5 * self._human_height
            else:
                # если рост человека равен None, то используем значение по умолчанию
                # вычисляем высоту нужного стула по выдуманной формуле

                return self._chair_height * 0.5 * self.__class__.default_human_height
                # альтернативный вариант записи:
                # return self._chair_height * 0.5 * Chair.default_human_height

    def set_chair_height(self, human_height):
        # вычисляем новую высоту стула по выдуманной формуле
        self._chair_height = 0.9 * human_height

    def del_chair_height(self):
        # теперь высота стула равна 0
        self._chair_height = 0

    chair_height = property(fget=get_chair_height,
                            fset=set_chair_height,
                            fdel=del_chair_height,
                            doc='Высота стула с учетом роста человека.')


print(Chair)    # <class '__main__.Chair'>
print(type(Chair.chair_height))  # <class 'property'>

help(Chair.chair_height)    # Help on property: Высота стула с учетом роста человека.

chair = Chair()
print(chair.chair_height)   # 1.5
chair.chair_height = 3
print(chair.chair_height)   # 2.295
del chair.chair_height
print(chair.chair_height)   # 0.0

# -------------------------------------------------
test_val = 5
print(test_val)     # 5
test_val = 1
del test_val
pass
