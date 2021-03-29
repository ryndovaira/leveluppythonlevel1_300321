def concat(*args, sep="/"):
    return sep.join(args)


ex1 = concat("earth", "mars", "venus")
print(ex1)  # earth/mars/venus

ex2 = concat("earth", "mars", "venus", sep=".")
print(ex2)  # earth.mars.venus
