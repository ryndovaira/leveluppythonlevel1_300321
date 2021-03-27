class First(object):
    def __init__(self):
        print("first")


class Second(First):
    def __init__(self):
        super().__init__()
        # First.__init__(self)
        print("second")


class Third(First):
    def __init__(self):
        super().__init__()
        # First.__init__(self)
        print("third")


class Fourth(Second, Third):
    def __init__(self):
        Second.__init__(self)   # эквивалентно super().__init__()
        Third.__init__(self)
        print("that's it")


f = Fourth()
# first
# second
# first
# third
# that's it
