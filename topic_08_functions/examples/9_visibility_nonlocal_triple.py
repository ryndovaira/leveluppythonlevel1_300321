x = 0


def outer():
    x = 1

    def inner():
        nonlocal x
        x = 2

        def inner_2():
            nonlocal x
            x = 3
            print("inner2:", x)

        inner_2()
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

print("global:", x)

# inner2: 3
# inner: 3
# outer: 3
# global: 0
