from enum import Enum, auto


class GameResult(Enum):
    W = auto()
    L = auto()
    E = auto()

# победа, проигрыш и ничья
# GameResult = Enum("GameResult", "W L E")
