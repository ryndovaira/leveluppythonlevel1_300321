acc = 0
for i in range(100):
    acc = acc + i
    double_sum = i + i
    print(f'double_sum = {double_sum}')
print('acc = ', acc)
# acc =  4950

print(list(range(10)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(5, 10)))
# [5, 6, 7, 8, 9]

print(list(range(5, 10, 2)))
# [5, 7, 9]

print(list(range(10, 5, -2)))
# [10, 8, 6]
