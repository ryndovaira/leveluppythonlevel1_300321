import pytest

from topic_07_oop.hw.class_4_1_pupil import Pupil


def test():
    name = 'Петя'
    age = 15
    marks = {
        'math': [3, 3, 3],
        'history': [4, 4, 5],
        'english': [5, 5, 4]
    }

    pupil = Pupil(name,
                  age,
                  marks)
    assert pupil.name == name
    assert pupil.age == age
    assert pupil.marks == marks

    assert sorted(pupil.get_all_marks()) == sorted([3, 3, 3, 4, 4, 5, 5, 5, 4])

    assert pupil.get_avg_mark() == 4
    assert pupil.get_avg_mark_by_subject('olol') == 0
    assert pupil.get_avg_mark_by_subject('math') == 3
    assert pupil.get_avg_mark_by_subject('history') == pytest.approx(4.33, 0.1)
    assert pupil.get_avg_mark_by_subject('english') == pytest.approx(4.66, 0.1)

    assert (pupil <= pupil) == True

    pupil_tmp1 = Pupil(name,
                       age,
                       {
                           'math': [5, 5, 5],
                           'history': [4, 4, 5],
                           'english': [5, 5, 4]
                       })
    assert (pupil <= pupil_tmp1) == True
    assert (pupil_tmp1 <= pupil) == False

    pupil_tmp2 = Pupil(name,
                       age,
                       {
                           'math': [3, 3, 3],
                           'history': [4, 4, 5],
                           'english': [3, 3, 3]
                       })

    assert (pupil <= pupil_tmp2) == False
    assert (pupil_tmp2 <= pupil) == True

