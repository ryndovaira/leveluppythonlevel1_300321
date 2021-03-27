# эквивалентно class Person:
# эквивалентно class Person():
class Person(object):   # эквивалентно class Person:# эквивалентно
    def __init__(self, first, last, age):
        self.firstname = first
        self.lastname = last
        self.age = age

    def __str__(self):
        return self.firstname + " " + self.lastname + ", " + str(self.age)

    def get_age_triple(self):
        return self.age * 3


class Employee(Person):
    def __init__(self, first, last, age, staff_num):
        super().__init__(first, last, age)
        self.staff_number = staff_num

    def __str__(self):
        return super().__str__() + ", " + self.staff_number

    def str_parent(self):
        return super().__str__()


class Student(Person):
    def __init__(self, first, last, age, avg_mark):
        super().__init__(first, last, age)
        self.avg_mark = avg_mark


class Empty(object):  # все в Python наследуется от object. эквивалентно class Invalid:
    # def __init__(self):
    #     pass
    ...


p = Person("Ivan", "Ivanov", 36)
e = Employee("Petr", "Petrov", 28, "1007")
s = Student('Masha', "Vasileva", 66, 4.8)


print(p)    # Ivan Ivanov, 36
print(e)    # Petr Petrov, 28, 1007
print(e.str_parent())   # Petr Petrov, 28

print(s)    # используется родительский метод __str__


# --------------------------
i = Empty()

print(i)    # <__main__.Empty object at 0x7fb2b73bad00>
