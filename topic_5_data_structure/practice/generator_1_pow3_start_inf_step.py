"""
Функция pow3_start_inf_step.

Принимает 2 аргумента: число start, step.

Возвращает генератор-выражение состоящий из
значений в 3 степени от start до бесконечности с шагом step.

Пример: start=3, step=2 результат 3^3, 5^3, 7^3, 9^3 ... (infinity).

Если start или step не являются int,
то вернуть строку 'Start and Step must be int!'.
"""