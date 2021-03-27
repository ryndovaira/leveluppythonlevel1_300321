import pytest

from topic_7_oop.hw.class_3_1_chicken import Chicken
from topic_7_oop.hw.class_3_2_goat import Goat
from topic_7_oop.hw.class_3_3_farm import Farm


def test():
    name = 'Ферма'
    owner = 'Петя'

    farm = Farm(name, owner)

    assert farm.name == name
    assert farm.owner == owner

    assert farm.get_animals_count() == 0
    assert farm.get_chicken_count() == 0
    assert farm.get_goat_count() == 0
    assert farm.get_milk_count() == 0
    assert farm.get_eggs_count() == 0

    farm.zoo_animals.extend([
        Chicken('Хохлуша', 1, 4),
        Chicken('Ряба', 1, 6),
        Chicken('Краснушка', 2, 5),

        Goat('Бешка', 3, 20),
        Goat('Дереза', 2, 15),
    ])

    assert farm.get_animals_count() == 5
    assert farm.get_chicken_count() == 3
    assert farm.get_goat_count() == 2
    assert farm.get_milk_count() == 35
    assert farm.get_eggs_count() == 15
