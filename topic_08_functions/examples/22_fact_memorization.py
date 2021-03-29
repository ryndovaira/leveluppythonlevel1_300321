def fact(n, accumulator=[1]):
    acc_len = len(accumulator)
    if acc_len <= n:
        for i in range(acc_len, n + 1):
            accumulator.append(i * accumulator[-1])
            print("computed for {}: {}".format(i, accumulator[i]))
    return accumulator[n]


print('f(3) = {}\n'.format(fact(3)))
# computed for 1: 1
# computed for 2: 2
# computed for 3: 6
# f(3) = 6

print('f(5) = {}\n'.format(fact(5)))
# computed for 4: 24
# computed for 5: 120
# f(5) = 120

print('f(3) = {}\n'.format(fact(3)))    # f(3) = 6
