for char in "qwertyu":
    print(char)

for index, char in enumerate("qwertyu"):
    print(f"index: {index}\t"
          f"char: {char}")
    if index % 2 == 0:
        print("Even!")

print('-' * 50)
