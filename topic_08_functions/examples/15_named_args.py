def hello(name, prefix="Hello, ", suffix="!"):
    print("{}{}{}".format(prefix, name, suffix))


hello(name="world")     # Hello, world!

hello(prefix="Hi ", name="world")   # Hi world!

hello("world", prefix="!!!!")       # !!!!world!
