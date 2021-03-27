def printc(arg1, arg2, *args, **kwargs):
    print(*kwargs)

    print(" ".join([arg1] + [arg2] + list(args) + list(kwargs.values())))


printc("1", "2", "3", "3", "3", "3", "3", four="4", five="5")   # 1 2 3 3 3 3 3 4 5
