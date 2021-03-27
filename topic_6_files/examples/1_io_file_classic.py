print('\n--------------------------------------- Read file (lines) ---------------------------------------------------')
# Прочитать файл file.txt и вывести его
# strip() убирает пробелы, табуляции и
# переносы строк из начала строки и конца
with open("file.txt", 'r') as f:
    # прочитать файл построчно
    for line in f:
        print(line.strip())
print('\n--------------------------------------- Read file (first 100) -----------------------------------------------')

with open("file.txt", 'r') as f:
    # прочитать весь файл целиком, если был вызван без аргументов,
    # и n символов, если был вызван с аргументом (целым числом n)
    print(f.read(100))

print('\n--------------------------------------- Write file (dict) ---------------------------------------------------')
my_dict = {'Python': '.py',
           'C++': '.cpp',
           'Java': '.java'}
with open("dict.txt", "w") as f:
    f.write(str(my_dict))

print('\n--------------------------------------- Write file (list) ---------------------------------------------------')
my_list = ['Python', 'C++', 'Java']
with open("list1.txt", "w") as f1, open("list2.txt", "w") as f2:
    f1.write(str(my_list))
    f2.write(str(my_list * 2))

# Эквивалентно
with open("list3.txt", "w") as f3:
    with open("list4.txt", "w") as f4:
        f3.write(str(my_list * 3))
        f4.write(str(my_list * 4))

# из одного файла читаем в другой пишем
with open("list3.txt", 'r') as f1, open("list3_eq.txt", 'w') as f2:
    f2.write(f1.read())
