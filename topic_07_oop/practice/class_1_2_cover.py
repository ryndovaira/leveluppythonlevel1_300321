class MyCover:
    """
    Класс Обложка
    Поля:
        автор
        год
    Методы:
        проверить авторство (сверить с параметром - именем автора)
        проверить год (раньше или позже определенного года)
        __str__
    """
    def __init__(self, a, y):
        self.author = a
        self.year = y

    def check_authority(self, writer):
        return writer == self.author

    def check_year(self, y):
        return "Early" if y < self.year else "Later"

    def __str__(self):
        return f"{self.author}, {self.year}"


if __name__ == '__main__':
    cover1 = MyCover('Чехов', 1890)

    # добавить новое поле для конкретного экземпляра
    cover1.bestseller = True

    # изменить значение поля экземпляра
    cover1.author = "Пушкин"
    # cover1.auhor = "Пушкин"

    print(cover1.check_year(1900))
    print(cover1.check_year(1800))
    print(cover1.check_authority("Пушкин"))
    print(cover1.check_authority("Чехов"))
    print(cover1)

    cover2 = MyCover('Marina', 2020)
    print(cover2)
