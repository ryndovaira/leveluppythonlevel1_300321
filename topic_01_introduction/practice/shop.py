"""
Ввод данных с клавиатуры:
- Магазин (наименование)
- Товар (наименование)
- Количество (товара)

Вывод данных в формате:
"Магазин называется '<Магазин>'. В нем имеется товар <Товар> в количестве <Количество>."
"""

shop = input('Магазин: ')
item = input('Товар: ')
count = input('Количество: ')

print("Магазин называется '", shop, "'. В нем имеется товар ", item, " в количестве ", count, ".", sep='')
