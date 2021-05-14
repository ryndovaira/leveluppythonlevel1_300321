import random

from project.combat.pokemon_npc import PokemonNPC
from project.combat.pokemon_state import PokemonState
from project.combat.pokemon_type import PokemonType
from project.combat.pokemon_types_weaknesses import pokemon_defence_weaknesses_by_type as weaknesses_by_type


class TestPokemonNPCClass:
    pokemon_name = 'Vulpix'  # определить после первого запуска теста
    pokemon_type = PokemonType.FIRE  # определить после второго запуска теста
    max_hp = 100

    def setup_method(self, method):
        """
        Этот метод будет выполняться перед каждым тестом из данного класса
        """
        # установить точку отсчета для случайных чисел
        random.seed(123)

    def test_init(self):
        pokemon_test = PokemonNPC()

        assert pokemon_test.name == self.__class__.pokemon_name
        assert pokemon_test.pokemon_type == self.__class__.pokemon_type
        assert pokemon_test.weaknesses == weaknesses_by_type[self.__class__.pokemon_type]
        assert pokemon_test.hp == self.__class__.max_hp
        assert pokemon_test.attack_point is None
        assert pokemon_test.defence_point is None
        assert pokemon_test.hit_power == 5
        assert pokemon_test.state == PokemonState.READY

    def test_str(self):
        pokemon_test = PokemonNPC()
        assert str(pokemon_test) == f"Name: {self.__class__.pokemon_name} | " \
                                    f"Type: {self.__class__.pokemon_type.name}\n" \
                                    f"HP: {self.__class__.max_hp}"
