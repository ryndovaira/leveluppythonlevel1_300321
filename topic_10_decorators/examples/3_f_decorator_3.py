def benchmark(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('Время выполнения: {} секунд.'.format(end - start))

    return wrapper


@benchmark
def do_useless_work():
    counter = 0
    for i in range(99999999):
        counter += i
    print(counter)


do_useless_work()
