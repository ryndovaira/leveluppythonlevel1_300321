from project.combat.pokemon_type import PokemonType
from project.combat.pokemon_types_weaknesses import pokemon_defence_weaknesses_by_type as weaknesses_by_type
from project.combat.body_part import BodyPart
from project.combat.pokemon_state import PokemonState


class Pokemon:
    def __init__(self,
                 name: str,
                 pokemon_type: PokemonType):
        self.name = name
        self.pokemon_type = pokemon_type
        self.weaknesses = weaknesses_by_type.get(pokemon_type, tuple())
        self.hp = 100
        self.attack_point = None
        self.defence_point = None
        self.hit_power = 5
        self.state = PokemonState.READY

    def __str__(self):
        return f"Name: {self.name} | Type: {self.pokemon_type.name}\nHP: {self.hp}"

    def next_step_points(self,
                         next_attack: BodyPart,
                         next_defence: BodyPart):
        self.attack_point = next_attack
        self.defence_point = next_defence

    def get_hit(self,
                opponent_attack_point: BodyPart,
                opponent_hit_power: int,
                opponent_type: PokemonType):
        if opponent_attack_point == BodyPart.NOTHING:
            return "Спасибо :)"
        elif self.defence_point == opponent_attack_point:
            return "Слабак!"
        else:
            self.hp -= opponent_hit_power * (3 if opponent_type in self.weaknesses else 1)

            if self.hp <= 0:
                self.state = PokemonState.DEFEATED
                return "Побежден :("
            else:
                return "Ранен, но не побежден!"


if __name__ == '__main__':
    p1 = Pokemon('ololol', PokemonType.DRAGON)
    print(p1)
