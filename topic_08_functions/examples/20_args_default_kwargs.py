def concat(*args, sep="/", **kwargs):
    return sep.join(args) + ' ' + str(kwargs)


ex1 = concat("earth", "mars", "venus", star='Sun')
print(ex1)  # earth/mars/venus {'star': 'Sun'}

ex2 = concat("earth", "mars", "venus", sep=".", other='Comets')
print(ex2)  # earth.mars.venus {'other': 'Comets'}
