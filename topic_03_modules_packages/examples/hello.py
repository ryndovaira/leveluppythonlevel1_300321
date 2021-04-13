# hello.py

# Код «инициализации» модуля
print('importing hello module')


def hello(name):
    return 'Hello, ' + name


def fun1(n1, n2):
    return n1 + n2


pi = 9

my_global_var = 123

if __name__ == '__main__':
    # тут полезная работа
    print("I'm in main function!")
    my_local_var = 99
