import enum


class PigeonState(enum.Enum):
    # name = (id, title) = value
    eating = (0, "Ест")
    sleeping = (1, "Спит")
    flying = (2, "Парит в небесах")

    def __init__(self, id, title):
        self.id = id
        self.title = title


if __name__ == '__main__':
    print(PigeonState.flying.name)
    print(PigeonState.flying.value)
    print(PigeonState.flying.id)
    print(PigeonState.flying.title)
