import pytest

from topic_7_oop.hw.class_1_human import Human


def test():
    age = 55
    first_name = 'Ira'
    last_name = 'Ryndova'

    human = Human(age, first_name, last_name)

    assert human.age == age
    assert human.get_age() == age

    assert human.first_name == first_name
    assert human.last_name == last_name

    human_tmp1 = Human(age, first_name, last_name)
    human_tmp2 = Human(age + 1, first_name, last_name)
    human_tmp3 = Human(age, first_name + "!", last_name)
    human_tmp4 = Human(age, first_name, last_name + "!")

    assert (human == human_tmp1) == True

    assert (human == human_tmp2) == False

    assert (human == human_tmp3) == False

    assert (human == human_tmp4) == False

    assert str(human) == f"Имя: {first_name} {last_name} Возраст: {age}"
