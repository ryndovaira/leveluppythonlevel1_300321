"""
Класс Pupil.

Поля:
имя: name,
возраст: age,
dict с оценками: marks (пример: {'math': [3, 5], 'english': [5, 5, 4] ...].

Методы:
get_all_marks: получить список всех оценок,
get_avg_mark_by_subject: получить средний балл по предмету (если предмета не существует, то вернуть 0),
get_avg_mark: получить средний балл (все предметы),
__le__: вернуть результат сравнения (<=) средних баллов (все предметы) двух учеников.
"""