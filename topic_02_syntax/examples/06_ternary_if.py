number = 3
oddity = 'odd' if number % 2 != 0 else 'even'
print(oddity)  # odd

# эквивалентно:
if number % 2 != 0:
    oddity = 'odd'
else:
    oddity = 'even'
