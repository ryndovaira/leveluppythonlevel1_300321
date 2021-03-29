import pytest

from topic_07_oop.hw.class_4_1_pupil import Pupil
from topic_07_oop.hw.class_4_2_worker import Worker
from topic_07_oop.hw.class_4_3_school import School


def test():
    pupil_1 = Pupil('Петя',
                    15,
                    {
                        'math': [3, 3, 3],
                        'history': [4, 4, 4],
                        'english': [5, 5, 5]
                    })
    pupil_2 = Pupil('Маша',
                    15,
                    {
                        'math': [4, 4, 4],
                        'history': [4, 4, 4],
                        'english': [4, 4, 4]
                    })

    pupil_3 = Pupil('Маша',
                    13,
                    {
                        'math': [5, 5, 5],
                        'history': [5, 5, 5],
                        'english': [5, 5, 5]
                    })

    worker_1 = Worker('Миша',
                      86324.50,
                      "Учитель математики")

    worker_2 = Worker('Лена',
                      56324.50,
                      "Повар")

    worker_3 = Worker('Василиса',
                      56324.50,
                      "Учитель математики")

    school = School([
                        pupil_1,
                        pupil_2,
                        pupil_3,

                        worker_1,
                        worker_2,
                        worker_3
                    ], 555
                    )

    assert school.get_avg_mark() == pytest.approx(4.3, 0.1)

    assert school.get_avg_salary() == pytest.approx(66324.5, 0.001)

    assert school.get_worker_count() == 3

    assert school.get_pupil_count() == 3

    assert sorted(school.get_pupil_names()) == sorted(['Петя', 'Маша', 'Маша'])

    assert sorted(school.get_unique_worker_positions()) == sorted(["Учитель математики", "Повар"])

    assert school.get_max_pupil_age() == 15

    assert school.get_min_worker_salary() == pytest.approx(56324.50, 0.0001)

    assert sorted(school.get_min_salary_worker_names()) == sorted(['Василиса', 'Лена'])
