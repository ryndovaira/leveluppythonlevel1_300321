from topic_07_oop.practice.class_1_1_page import MyPage


class Book:
    """
    Класс Книга
    Поля:
        страницы,
        название (каждое слово с большой буквы, остальные маленькие),
        автор,
        год издания
    Методы:
        добавить страницу в конец,
        добавить несколько страниц в конец,
        вывести весь контент,
        __len__: получить количество страниц,
        вернуть все четные страницы
        __invert__(~): вернуть результат реверса строки с названием
        (например, было "Крутая Книга", а стало "Агинк Яатурк").
        __add__(+): добавить к году число
    """

    def __init__(self, name: str, author: str, year: int):
        self.name = name.title()
        self.author = author
        self.year = year
        self.pages = []

    def add_one_page(self, page: MyPage):
        self.pages.append(page)

    def add_some_pages(self, pages: list):
        self.pages.extend(pages)

    def print_all(self):
        for page in self.pages:
            print(page)

    def __len__(self):
        return len(self.pages)

    def get_even_pages(self):
        return [page for page in self.pages if page.num_page % 2 == 0]

    def __invert__(self):
        return self.name[::-1].title()

    def __add__(self, other):
        self.year += other
        return self.year


if __name__ == '__main__':
    book = Book("My best book", "Nikolay", 2021)
    page1 = MyPage(1, "Начало")
    pages234 = [MyPage(2, "Продолжение"),
                MyPage(3, "Задумчивость"),
                MyPage(4, "Развязка")]

    book.add_one_page(page1)

    book.add_some_pages(pages234)

    book.print_all()

    print(len(book))

    print([str(page) for page in book.get_even_pages()])
    print(*book.get_even_pages(), sep=" | ")

    print(~book)

    print(book + 5)
    print(book.year)
