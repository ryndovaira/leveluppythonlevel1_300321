import pytest

from topic_7_oop.hw.class_3_2_goat import Goat


def test():
    name = 'Ряба'
    age = 6
    milk_per_day = 20

    goat = Goat(name, age, milk_per_day)

    assert goat.age == age
    assert goat.name == name
    assert goat.milk_per_day == milk_per_day

    assert goat.get_sound() == 'Бе-бе-бе'

    assert (~goat).name == 'Абяр'

    assert (goat * 3).milk_per_day == milk_per_day * 3
