x = 0


def outer():
    # SyntaxError: no binding for nonlocal 'x' found
    # nonlocal x
    x = 1

    def inner():
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

print("global:", x)

# inner: 2
# outer: 2
# global: 0