import pytest

from topic_7_oop.hw.class_2_movie import Movie


def test_human():
    duration_min = 90
    name = 'Funny movie'
    year = 2010

    movie = Movie(duration_min, name, year)

    assert movie.duration_min == duration_min
    assert movie.name == name
    assert movie.year == year

    assert str(movie) == f'Наименование фильма: {name} | Год выпуска: {year} | Длительность (мин): {duration_min}'

    movie_tmp1 = Movie(duration_min, name, year)
    assert (movie >= movie_tmp1) == True

    movie_tmp2 = Movie(duration_min + 20, name, year)
    assert (movie >= movie_tmp2) == False

    movie_tmp3 = Movie(duration_min - 20, name, year)
    assert (movie >= movie_tmp3) == True


