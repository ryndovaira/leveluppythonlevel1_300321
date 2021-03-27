class BeautifulChair:
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

    # помечаем, то chair_height - это свойство

    # одновременно является и getter
    @property
    def chair_height(self):
        """Это свойство chair_height."""
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

    @chair_height.setter
    def chair_height(self, human_height):
        # вычисляем новую высоту стула по выдуманной формуле
        self._chair_height = 0.9 * human_height

    @chair_height.deleter
    def chair_height(self):
        # теперь высота стула равна 0
        self._chair_height = 0


print(type(BeautifulChair.chair_height))    # <class 'property'>

help(BeautifulChair.chair_height)           # Help on property: Это свойство chair_height.

my_beautiful_chair = BeautifulChair()

print(my_beautiful_chair.chair_height)      # 1.5

my_beautiful_chair.chair_height = 3
print(my_beautiful_chair.chair_height)      # 2.295

del my_beautiful_chair.chair_height
print(my_beautiful_chair.chair_height)      # 0.0
