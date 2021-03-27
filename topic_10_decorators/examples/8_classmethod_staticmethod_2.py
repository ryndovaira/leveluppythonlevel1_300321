from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name_var, year_var):
        return cls(name_var, date.today().year - year_var)

    @staticmethod
    def is_adult_person(person):
        return person.age > 18

    @staticmethod
    def is_adult(person_age):
        return person_age > 18


person1 = Person('Ivan', 25)
person2 = Person.from_birth_year('Rosa', 1994)
print(person1.name, person1.age)  # Ivan 25
print(person2.name, person2.age)  # Rosa 26
print(Person.is_adult_person(person1))  # True
print(Person.is_adult(25))  # True
print(Person.is_adult(17))  # False
