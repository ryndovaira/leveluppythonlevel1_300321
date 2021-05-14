import random

from project.combat.pokemon import Pokemon
from project.combat.pokemon_type import PokemonType
from project.combat.pokemon_by_type import pokemon_by_type
from project.combat.body_part import BodyPart


class PokemonNPC(Pokemon):
    def __init__(self):
        rand_type_value = random.randint(PokemonType.min_value(), PokemonType.max_value())
        rand_pokemon_type = PokemonType(rand_type_value)

        rand_pokemon_name = random.choice(list(pokemon_by_type.get(rand_pokemon_type, {}).keys()))

        super().__init__(rand_pokemon_name, rand_pokemon_type)

    # для избежания проблем связанных с наследованием добавим аргумент заглушку **kwargs
    # или можно переименовать метод
    # или игнорировать warning
    def next_step_points(self, **kwargs):
        attack_point = BodyPart(random.randint(BodyPart.min_value(), BodyPart.max_value()))
        defence_point = BodyPart(random.randint(BodyPart.min_value(), BodyPart.max_value()))
        super().next_step_points(next_attack=attack_point,
                                 next_defence=defence_point)


if __name__ == '__main__':
    pokemon_npc = PokemonNPC()
    pokemon_npc.next_step_points()
    print(pokemon_npc)
