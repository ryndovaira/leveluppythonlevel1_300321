# fib.py

def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()


def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


fib(n=2000)  # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
fib2(n=2000)  # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
