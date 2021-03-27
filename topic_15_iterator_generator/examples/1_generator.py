def generator(n):
    for y in range(0, n):
        yield y


def return_fun(n):
    for k in range(0, n):
        return k


return_res = return_fun(55)
print(f'return_res = {return_res}')

my_range = generator(10)
print(list(my_range))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in generator(10):
    print(i, end='---')

try:
    new_range = generator(1)
    print(next(new_range))  # 0
    next(new_range)  # StopIteration
except StopIteration as si:
    print('Generator is empty!')


