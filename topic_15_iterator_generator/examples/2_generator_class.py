class Generator:
    counter = 0

    def __init__(self, number):
        self.number = number

    def __next__(self):
        if self.__class__.counter < self.number:
            result = self.__class__.counter
            self.__class__.counter += 1
            return result
        else:
            raise StopIteration()

    def __iter__(self):
        return self


newest = Generator(5)
print(f'list(newest): {list(newest)}')
print(f'Generator.counter: {Generator.counter}')
print(f'newest.counter: {newest.counter}')
Generator.counter = 9
newest.counter = 7      # ВНИМАНИЕ: создали новое поле экземпляра!
print(f'Generator.counter: {Generator.counter}')
print(f'newest.counter: {newest.counter}')

newest.number = 12
for i in newest:
    print(i)
