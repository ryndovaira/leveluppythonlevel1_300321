print('Hello, {}!'.format('Vasya'))

print('{0}, {1}, {2}'.format('a', 'b', 'c'))

print('{}, {}, {}'.format('a', 'b', 'c'))

print('{2}, {1}, {0}'.format('a', 'b', 'c'))

print('{2}, {1}, {0}'.format(*'abc'))

print('{0}{1}{0}'.format('abra', 'cad'))


print('------------------------------------------------------------------------------------------------------------')
print('-------------------------------------------- Advanced information ------------------------------------------')

print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))

coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print('Coordinates: {latitude}, {longitude}'.format(**coord))

coord = (3, 5)
print('X: {0[0]};  Y: {0[1]}'.format(coord))

print("repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2'))

print('{:<30}'.format('left aligned'))

print('{:>30}'.format('right aligned'))

print('{:^30}'.format('centered'))

print('{:*^30}'.format('centered'))     # use '*' as a fill char

print('{:+f}; {:+f}'.format(3.14, -3.14))   # show it always

print('{: f}; {: f}'.format(3.14, -3.14))   # show a space for positive numbers

print('{:-f}; {:-f}'.format(3.14, -3.14))   # show only the minus -- same as '{:f}; {:f}'

# format also supports binary numbers
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))

# with 0x, 0o, or 0b as prefix:
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))

points = 19.5
total = 22
print('Correct answers: {:.2%}'.format(points/total))
