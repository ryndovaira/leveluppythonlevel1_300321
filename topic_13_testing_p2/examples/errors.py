def divide(x, y):
    if y == 0:
        raise ZeroDivisionError('my zero error')
    return x / y


def my_error():
    raise Exception('my error text')
