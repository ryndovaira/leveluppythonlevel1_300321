x = 0


def outer():
    x = 1

    def inner():
        global x
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

print("global:", x)

# inner: 2
# outer: 1
# global: 2