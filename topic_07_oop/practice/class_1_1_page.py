class MyPage:
    """
    Класс Страница
    Поля:
        номер страницы
        контент
    Методы:
        вывести контент (конвертация к строке)
        поиск строки в контенте (содержится ли строка в контенте?)
    """

    def find_my_str(self, val):
        if val in self.content:
            print(f"{val} found in content!")
        else:
            print(f"{val} not found in content!")

    # вызывается по имени класса
    def __init__(self, n_page, content):
        self.num_page = n_page
        self.content = content

    def find_2(self, val):
        return self.content.find(val)

    # стандартный результат <__main__.MyPage object at 0x7f73ac0264f0>
    def __str__(self):
        return f"{self.num_page}: {self.content}"


if __name__ == "__main__":
    page1 = MyPage(1, "lalalalapo")

    if type(page1) == MyPage:
        print("It's MyPage instance!")
    else:
        print('Something wrong!')

    # эквивалентно:
    if isinstance(page1, MyPage):
        print("It's MyPage instance!")
    else:
        print('Something wrong!')

    conv_to_str = str(page1)

    print(page1)
    page1.find_my_str("la")
    page1.find_my_str("ba")

    print(page1.find_2('ala'))
    print(page1.find_2('o'))
    print(page1.find_2('b'))
