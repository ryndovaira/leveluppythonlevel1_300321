def my_ex_fun1(p1, p2):
    if p1 > 5:
        print("p1 > 5")
    elif p2 > 10:
        print("p2 > 10")
    elif p1 == p2:
        print("p1 == p2")
    else:
        print("It' else block!")


def my_ex_fun2(p1, p2):
    if p1 > 5:
        print("p1 > 5")
    if p2 > 10:
        print("p2 > 10")
    if p1 == p2:
        print("p1 == p2")
    else:
        print("It' else block!")


if __name__ == '__main__':
    my_ex_fun1(6, 6)
    print("-" * 50)
    my_ex_fun2(6, 6)
    print("*" * 50)

    my_ex_fun1(6, 11)
    print("-" * 50)
    my_ex_fun2(6, 11)
