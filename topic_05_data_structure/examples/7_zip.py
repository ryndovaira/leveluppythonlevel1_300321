from itertools import zip_longest

print('\n--------------------------------------- Common --------------------------------------------------------------')
ex_common = list(zip([0, 1, 2], "012", ("zero", "one", "two")))
print(ex_common)  # [(0, '0', 'zero'), (1, '1', 'one'), (2, '2', 'two')]

ex_one_arg = list(zip('012'))
print(ex_one_arg)  # [('0',), ('1',), ('2',)]

ex_with_dict = list(zip([0, 1, 2], "012", {0: "zero", 1: "one", 2: "two"}))
print(ex_with_dict)  # [(0, '0', 0), (1, '1', 1), (2, '2', 2)]

ex_with_dict_val = list(zip([0, 1, 2], "012", {0: "zero", 1: "one", 2: "two"}.values()))
print(ex_with_dict_val)  # [(0, '0', 'zero'), (1, '1', 'one'), (2, '2', 'two')]

ex_long = list(zip_longest([1], 'abcd', (9, 8, 7), fillvalue='?'))
print(ex_long)  # [(1, 'a', 9), ('?', 'b', 8), ('?', 'c', 7), ('?', 'd', '?')]

print('\n--------------------------------------- For (list) ----------------------------------------------------------')
letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
for l, n in zip(letters, numbers):
    print(f'Letter: {l} | Number: {n}')

print('\n--------------------------------------- For (dict) ----------------------------------------------------------')
dict_one = {'first_name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
dict_two = {'name': 'Jane', 'last_name': 'Doe', 'occupation': 'Community Manager'}
for ((k1, v1), (k2, v2)) in zip(dict_one.items(), dict_two.items()):
    print(f'{k1} -> {k2} | {v1} -> {v2}')

print('\n--------------------------------------- Advanced: Unzip (*, **) ---------------------------------------------')
pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
pairs_2 = [1, 'a', 2, 'b', 3, 'c', 4, 'd']
my_dict = {'f': 77, '333': 'yyy'}
numbers, letters = zip(*pairs)
print(*pairs)
print(*pairs_2)
print(f'numbers: {numbers}')
print(f'letters: {letters}')
