def concat(*args, sep="/", **kwargs):
    return sep.join(args) + ' ' + str(kwargs)


ex1 = concat("earth", "mars", "venus", '.', star='Sun', other2='Comets2')
print(ex1)  # earth/mars/venus {'star': 'Sun'}

ex2 = concat("earth", "mars", "venus", sep=".", other='Comets', other2='Comets2')
print(ex2)  # earth.mars.venus {'other': 'Comets'}

# sep в начало не нельзя, только после всех *args
# но можно в любом месте после *args
ex3 = concat("earth", "mars", "venus", other='Comets', other2='Comets2', sep=".")

ex4 = concat("earth", "mars", "venus", other='Comets', sep=".", other2='Comets2')

