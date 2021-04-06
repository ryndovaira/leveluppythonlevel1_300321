a = 5 + 6

b = (5).__add__(6)

print(a, b)

print(4 == 4.0)
print(4 == "4")

c = 5 > 6
print(c)

if 123:
    print('123!')

if 0:
    print("0!")

if "lalala":
    print("I'm here!")

if "":
    print("It' empty!")

age = 30
name = "Olga"
lname = 'Petrova'
if (age > 25 and name == "Olga") or lname == 'Petrova':
    print('Bingo')

if not (age < 30):
    print('!!!')

# --------------------------

if age >= 30 or name == 'Olga':
    print('Cool!')

if name == 'Pete' and age == 30:
    print('Unreal!')
else:
    print('Always here')

# ---------------------------

age = 101
if age == 30:
    print(f'{age} лет')
elif age == 3:
    print(f'{age} года')
elif age == 100:
    print("не ври мне!")
else:
    print('в остальных случаях')

# ----------------------------

if age > 25:
    print("!")
elif age < 5:
    print("?")

# ---------

if age > 10:
    print('Yes')

# ----------------

for my_new_val in range(5):
    print(my_new_val)

print(range(5))
