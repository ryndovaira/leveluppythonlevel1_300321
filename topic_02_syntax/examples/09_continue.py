for i in 'hello world':
    if i == 'o':
        continue
    print(i * 2, end='')

# hheellll  wwrrlldd

a = '\n' * 3 + '*' * 50

print(f"{a}\n")

x = 5
while x < 20:
    x += 2
    # if x == 7 or x == 9 or x == 11:
    if x in (7, 9, 11):
        print('Skip it')
        continue
        print("I'm here")  # недостижим
    print(f"моя переменная равна {x}")

print('lalala')
