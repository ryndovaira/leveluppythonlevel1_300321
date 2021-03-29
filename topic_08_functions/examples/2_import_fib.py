import fib

# Можно обращаться к определениям из fib
fib.fib(100)
# 1 1 2 3 5 8 13 21 34 55 89

print(fib.fib2(100))
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print(fib.__name__)
# fib

fib_alt = fib.fib
fib_alt(100)
# 1 1 2 3 5 8 13 21 34 55 89
