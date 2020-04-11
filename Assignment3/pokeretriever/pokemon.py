import abc


class PokedexObject(abc.ABC):
    def __init__(self, name: str, id: int):
        self.id = id
        self.name = name


class PokemonMove(PokedexObject):
    def __init__(self, name: str, level_learned: int, id: int, generation: str, accuracy: int, pp: int, power: int, type: str,
                 damage_class: str, effect_short: str):
        super().__init__(name, id)
        self.level_learned = level_learned  # Only given in pokemon entry not ability entry, might be nothing
        self.generation = generation  # Expanded only
        self.accuracy = accuracy  # Expanded only
        self.pp = pp  # Expanded only
        self.power = power  # Expanded only
        self.type = type  # Expanded only
        self.damage_class = damage_class  # Expanded only
        self.effect_short = effect_short  # Expanded only

    def __str__(self):

        expanded_condition = False  # This needs to be defined at some point, this is just representational

        if not expanded_condition:
            return f"---- Name: {self.name} ----\n" \
                   f"Learned at Level: {self.level_learned}"
        elif expanded_condition:
            return f"---- Name: {self.name} ----\n" \
                   f"ID: {self.id}\n" \
                   f"Learned at Level: {self.level_learned}\n" \
                   f"Generation: {self.generation}\n" \
                   f"Accuracy: {self.accuracy}\n" \
                   f"Power Points: {self.pp}\n" \
                   f"Power: {self.power}\n" \
                   f"Type: {self.type}\n" \
                   f"Damage Class: {self.damage_class}\n" \
                   f"Effect (Short): {self.effect_short}"


class PokemonStat(PokedexObject):
    def __init__(self, name: str, base_value: int, id: int, is_battle_only: bool):
        super().__init__(name, id)
        self.base_value = base_value  # Only given in pokemon entry not ability entry, might be nothing
        self.is_battle_only = is_battle_only  # Expanded only

    def __str__(self):

        expanded_condition = False  # This needs to be defined at some point, this is just representational

        if not expanded_condition:
            return f"---- Name: {self.name} ----\n" \
                   f"Base Value: {self.base_value}"
        elif expanded_condition:
            return f"---- Name: {self.name} ----\n" \
                   f"ID: {self.id}\n" \
                   f"Base Value: {self.base_value}\n" \
                   f"Is Battle Only: {self.is_battle_only}"


class PokemonAbility(PokedexObject):
    def __init__(self, name: str, id: int, generation: str, effect: str, effect_short: str, pokemon: list):
        super().__init__(name, id)
        self.generation = generation  # Expanded only
        self.effect = effect  # Expanded only
        self.effect_short = effect_short  # Expanded only
        self.pokemon = pokemon  # Expanded only

    def __str__(self):

        expanded_condition = False  # This needs to be defined at some point, this is just representational

        if not expanded_condition:
            return f"---- Name: {self.name} ----\n" \
                   f"ID: {self.id}"
        elif expanded_condition:
            return f"---- Name: {self.name} ----\n" \
                   f"ID: {self.id}\n" \
                   f"Generation: {self.generation}\n" \
                   f"Effect: {self.effect}\n" \
                   f"Effect (Short): {self.effect_short}\n" \
                   f"Pokemon: {self.pokemon}"


class Pokemon(PokedexObject):
    def __init__(self, name: str, id: int, height: int, weight: int, stats: list, types: list,
                 abilities: list, moves: list):
        super().__init__(name, id)
        self.height = height
        self.weight = weight
        self.moves = moves
        self.abilities = abilities
        self.types = types
        self.stats = stats

    def __str__(self):
        return f"---- Name: {self.name} ----\n" \
               f"ID: {self.id}\n" \
               f"Height: {self.height}\n" \
               f"Weight: {self.weight}\n" \
               f"Moves: {self.moves}\n" \
               f"Abilities: {self.abilities}\n" \
               f"Types: {self.types}\n" \
               f"Stats: {self.stats}"
