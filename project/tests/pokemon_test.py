from project.combat.pokemon import Pokemon
from project.combat.pokemon_state import PokemonState
from project.combat.pokemon_type import PokemonType
from project.combat.pokemon_types_weaknesses import pokemon_defence_weaknesses_by_type as weaknesses_by_type


class TestPokemonClass:
    pokemon_name = 'Pikachu'
    pokemon_type = PokemonType.ELECTRIC
    max_hp = 100

    def test_init(self):
        pokemon_test = Pokemon(name=self.__class__.pokemon_name,
                               pokemon_type=self.__class__.pokemon_type)

        assert pokemon_test.name == self.__class__.pokemon_name
        assert pokemon_test.pokemon_type == self.__class__.pokemon_type
        assert pokemon_test.weaknesses == weaknesses_by_type[self.__class__.pokemon_type]
        assert pokemon_test.hp == self.__class__.max_hp
        assert pokemon_test.attack_point is None
        assert pokemon_test.defence_point is None
        assert pokemon_test.hit_power == 5
        assert pokemon_test.state == PokemonState.READY

    def test_str(self):
        pokemon_test = Pokemon(name=self.__class__.pokemon_name,
                               pokemon_type=self.__class__.pokemon_type)
        assert str(pokemon_test) == f"Name: {self.__class__.pokemon_name} | " \
                                    f"Type: {self.__class__.pokemon_type.name}\n" \
                                    f"HP: {self.__class__.max_hp}"
