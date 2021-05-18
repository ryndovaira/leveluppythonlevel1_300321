from enum import Enum, auto


class PokemonState(Enum):
    READY = auto()
    DEFEATED = auto()

# короткая запись
# PokemonState = Enum('PokemonState', "READY DEFEATED")
