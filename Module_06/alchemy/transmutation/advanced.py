from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone():
    stone_ingredient = lead_to_gold()
    potion_ingredient = healing_potion()
    return (f"Philosopher's stone created using {stone_ingredient} "
            f"and {potion_ingredient}")


def elixir_of_life():
    return "Elixir of life: eternal youth achieved!"
