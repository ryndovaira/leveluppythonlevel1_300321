from enum import Enum

# class PokemonState(Enum):
#     READY = auto()
#     DEFEATED = auto()

# короткая запись
PokemonState = Enum('PokemonState', "READY DEFEATED")
