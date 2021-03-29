# Файл fib_input.py

def fib(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b

    return result


if __name__ == "__main__":
    import sys
    print(sys.argv[0])
    n = int(sys.argv[1])

    fib_list = fib(n)
    print(" ".join(map(str, fib_list)))
