print('\n--------------------------------------- List Comprehension --------------------------------------------------')

square = [x ** 2 for x in range(10)]
# square = []
# for x in range(10):
#     square.append(x ** 2)

print(square)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print('\n-------------------------------------------------------------------------------------------------------------')

odds_tmp = [x for x in range(10) if x % 2 != 0]
odds = []
for x in range(10):
    if x % 2 != 0:
        odds.append(x)
print(odds)  # [1, 3, 5, 7, 9]

print('\n-------------------------------------------------------------------------------------------------------------')

lst_ex = [[int(i == j) for i in range(3)] for j in range(3)]
print(lst_ex)  # [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

lst_tmp = []
for j in range(3):
    for i in range(3):
        lst_tmp.append(int(i == j))

print('\n-------------------------------------------------------------------------------------------------------------')

lst_pair_ex = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(lst_pair_ex)  # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

print('\n--------------------------------------- Tuple Comprehension -------------------------------------------------')

tuple_1 = tuple(n ** n for n in range(5))
print(tuple_1)
# (1, 1, 4, 27, 256)

tuple_2 = tuple(n ** 2 for n in (1, 33, 3, 444, 5, 6, 999) if n % 2 == 0)
print(tuple_2)
# (197136, 36)

lst = ['hello', 'hi', 'hello', 'today', 'morning', 'again', 'hello']
tuple_3 = tuple(lst.count(k) * k for k in lst)
print(tuple_3)
# ('hellohellohello', 'hi', 'hellohellohello', 'today', 'morning', 'again', 'hellohellohello')

print('\n--------------------------------------- Set Comprehension --------------------------------------------------')
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
my_set = {i for i in list_a}
print(my_set)  # {0, 1, 2, 3, 4, 5, -1, -2} - порядок случаен

print('\n--------------------------------------- Dict Comprehension --------------------------------------------------')

dc_1 = {n: n ** 2 for n in range(5)}
print(dc_1)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

dc_2 = {n ** 2: True for n in range(5)}
print(dc_2)
# {0: True, 1: True, 4: True, 9: True, 16: True}

lst = ['hello', 'hi', 'hello', 'today', 'morning', 'again', 'hello']
dc_3 = {k: lst.count(k) for k in lst}
print(dc_3)
# {'hello': 3, 'hi': 1, 'today': 1, 'morning': 1, 'again': 1}
