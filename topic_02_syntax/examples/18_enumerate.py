for char in "qwertyu":
    print(char)

for index, char in enumerate("qwertyu"):
    print(f"index: {index}\t"
          f"char: {char}")
    if index % 2 == 0:
        print("Even!")

print('-' * 50)

# ------------------------------------
my_list = [1, 'tytyt', 2, 3]

for index, element in enumerate(my_list):
    print(f"index: {index}\t"
          f"element: {element}")

print('-' * 50)

my_dict = {1: 'a', 2: 'b', 44: 'zz'}
for index, (key, value) in enumerate(my_dict.items()):
    print(f"index: {index}\t"
          f"key: {key}\t"
          f"value: {value}")

print('-' * 50)
# ИЛИ

for index, key_value in enumerate(my_dict.items()):
    print(f"index: {index}\t"
          f"key: {key_value[0]}\t"
          f"value: {key_value[1]}\t"
          f"key_value: {key_value}")

print('-' * 50)

my_set = {1, 2, 3, 2, 1}
for index, element in enumerate(my_set):
    print(f"index: {index}\t"
          f"element: {element}")
