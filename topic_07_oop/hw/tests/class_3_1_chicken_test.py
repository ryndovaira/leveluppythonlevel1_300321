import pytest

from topic_07_oop.hw.class_3_1_chicken import Chicken


def test():
    name = 'Ряба'
    corral_num = 6
    eggs_per_day = 20

    chicken = Chicken(name, corral_num, eggs_per_day)

    assert chicken.corral_num == corral_num
    assert chicken.name == name
    assert chicken.eggs_per_day == eggs_per_day

    assert chicken.get_sound() == 'Ко-ко-ко'

    assert chicken.get_info() == f'Имя курицы: {name}\nНомер загона: {corral_num}\nКоличество яиц в день: {eggs_per_day}'

    chicken_tmp1 = Chicken(name, corral_num, eggs_per_day)
    assert (chicken < chicken_tmp1) == False

    chicken_tmp2 = Chicken(name, corral_num, eggs_per_day + 1)
    assert (chicken < chicken_tmp2) == True

    chicken_tmp3 = Chicken(name, corral_num, eggs_per_day - 1)
    assert (chicken < chicken_tmp3) == False


