def hello(name, prefix="Hello, ", suffix="!"):
    print("{}{}{}".format(prefix, name, suffix))


hello("world")  # Hello, world!

hello("world", "Hi ")   # Hi world!

hello("world", "Hi ", "!!!!")   # Hi world!!!!

