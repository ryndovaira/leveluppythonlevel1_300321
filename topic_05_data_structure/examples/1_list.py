print('\n--------------------------------------- Introduction --------------------------------------------------------')

squares = [1, 4, 9, 16, 25]
miscellaneous = [1, True, None, int, print, "Hello world"]
print('len(miscellaneous) = ', len(miscellaneous))
# len(miscellaneous) =  6

miscellaneous[4]('I can use it!')

print('\n--------------------------------------- Indexes and slices --------------------------------------------------')

names = ["Dries", "Romeo", "Kevin", "Eden", "Thibaut", "Jan", "Micky"]

print(names[-4])
# 'Eden'

print(names[:2])
# ['Dries', 'Romeo']

print(names[::-1])
# ['Micky', 'Jan', 'Thibaut', 'Eden', 'Kevin', 'Romeo', 'Dries']

print(names[2:7:2])
# ['Kevin', 'Thibaut', 'Micky']


print('\n--------------------------------------- Operators -----------------------------------------------------------')

names = ["Dries", "Romeo", "Kevin", "Eden", "Thibaut", "Jan", "Micky"]

del names[0]
print(names)
# ['Romeo', 'Kevin', 'Eden', 'Thibaut', 'Jan', 'Micky']

del names[::2]
print(names)
# ['Kevin', 'Thibaut', 'Micky']

names[2] = 'Thorn'
print(names)
# ['Kevin', 'Thibaut', 'Thorn']

print(names + ['Jan', 'Vincent', 'Thomas'])
# ['Kevin', 'Thibaut', 'Thorn', 'Jan', 'Vincent', 'Thomas']

print(names * 3)
# ['Kevin', 'Thibaut', 'Thorn', 'Kevin', 'Thibaut', 'Thorn', 'Kevin', 'Thibaut', 'Thorn']


print('\n--------------------------------------- Details -------------------------------------------------------------')

lst = []
lst.append(lst)
print(lst)  # [[...]]
lst.append(1)
print(lst)  # [[...], 1]
print(lst[0])  # [[...], 1]
print(lst[0][1])  # 1

lst1 = [1, 3, 'to', False]
print(f'lst1: {lst1}')  # [1, 3, 'to', False]

lst2 = ['ttt', 3, 'ppp', True]
print(f'lst2: {lst2}')  # ['ttt', 3, 'ppp', True]

lst3 = lst1 + lst2
print(f'lst3: {lst3}')  # [1, 3, 'to', False, 'ttt', 3, 'ppp', True]

lst1.extend(lst2)
print(f'lst1 (after extend): {lst1}')  # [1, 3, 'to', False, 'ttt', 3, 'ppp', True]

lst2 += lst1
print(f'lst2 (after concat with lst1): {lst2}')  # ['ttt', 3, 'ppp', True, 1, 3, 'to', False, 'ttt', 3, 'ppp', True]

print('\n--------------------------------------- Split and Join ------------------------------------------------------')

print('1,2,3'.split(','))  # ['1', '2', '3']

print("-".join(['1', '2', '3']))  # 1-2-3

print('\n--------------------------------------- Copy (mutable) ------------------------------------------------------')
my_list_1 = [0, 1, 2, 3]
my_list_2 = my_list_1.copy()  # !!!
print(my_list_1, my_list_2)

my_list_1.append(99)
my_list_2.append(33)
print(my_list_1, my_list_2)


# ----------------------------------------------

def func(my_list: list):
    my_list.append(777)
    my_list.extend(['qqq', 123])


my_list_original = [0, 1]

func(my_list_original)

print(my_list_original)     # [0, 1, 777, 'qqq', 123]
