import random


def get_random():
    """
    Получить случайное число [0, 10)
    :return: случайное число [0, 10)
    """
    return random.randint(0, 9)


if __name__ == '__main__':
    help(get_random)
    help(random.randint)

    rand_int = get_random()
    print(rand_int)
    if rand_int == 5:
        print("You are lucky!")
    else:
        print("Boo...")
