from typing import Callable
from functools import reduce, partial, lru_cache, singledispatch


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        total = reduce(lambda x, y: x + y, spells)
    elif operation == "multiply":
        total = reduce(lambda x, y: x * y, spells)
    elif operation == "max":
        total = reduce(lambda x, y: x if x > y else y, spells)
    elif operation == "min":
        total = reduce(lambda x, y: x if x < y else y, spells)
    else:
        total = 0
    return total


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        'fire_enchant': partial(base_enchantment, power=50, element='fire'),
        'ice_enchant': partial(base_enchantment, power=50, element='ice'),
        'lightning_enchant': partial(base_enchantment,
                                     power=50,
                                     element='lightning')
    }


def enchant(target: str, power: int, element: str) -> str:
    return f"{target} + {element} ({power} power)"


@lru_cache(maxsize=128)
def memorized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memorized_fibonacci(n - 1) + memorized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def cast_spell(spell):
        return f"Unknown spell type: {type(spell).__name__}"

    @cast_spell.register(int)
    def _(spell: int):
        return f"Damage spell: {spell} points!"

    @cast_spell.register(str)
    def _(spell: str):
        return f"Enchantment: {spell}"

    @cast_spell.register(list)
    def _(spell: list):
        spell_count = len(spell)
        spell_names = ', '.join(map(str, spell))
        return f"Multi-cast: {spell_count} spells ({spell_names})"
    return cast_spell


def main() -> None:
    spell1 = {"name": "fireball", "power": 1}
    spell2 = {"name": "mega fireball", "power": 5}
    spell3 = {"name": "crystal orb", "power": 2}
    spell4 = {"name": "mega crystal orb", "power": 10}
    spells = [
        spell1["power"],
        spell2["power"],
        spell3["power"],
        spell4["power"]
    ]
    print("Testing spell reducer...")
    print(f"sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    print(f"Min: {spell_reducer(spells, 'min')}")
    enchants = partial_enchanter(enchant)
    print("\nTesting partial enchanter...")
    print(enchants['fire_enchant']("Sword"))
    print(enchants['ice_enchant']("Shield"))
    print(enchants['lightning_enchant']("Staff"))
    print("\nTesting memorized fibonacci...")
    print(f"fibonacci 5: {memorized_fibonacci(5)}")
    print(f"fibonacci 10: {memorized_fibonacci(10)}")
    print(f"fibonacci 25: {memorized_fibonacci(25)}")
    print(f"fibonacci 50: {memorized_fibonacci(50)}")
    print("\nTesting spell dispatcher...")
    cast_spell = spell_dispatcher()
    print("int")
    damage_values = [10, 50, 100, 250]
    for damage in damage_values:
        print(cast_spell(damage))
    print("\nString")
    enchantments = ["Fireball",
                    "Heal",
                    "Shield",
                    "Lightning Bolt",
                    "Ice Storm"]
    for x in enchantments:
        print(cast_spell(x))
    print()
    print("Multi-cast")
    multi_casts = [
        ["heal", "shield"],
        ["fireball", "lightning", "ice"],
        ["buff", "protect", "regenerate", "haste"],
        [1, 2, 3, 4, 5]
    ]
    for spells in multi_casts:
        print(cast_spell(spells))
    print()
    print("Unknown Types")
    unknown_types = [
        3.14,                           # float
        (100, "fire"),                  # tuple
        {"spell": "fireball"},          # dict
        {1, 2, 3},                      # set
        None                            # None
    ]
    for spell in unknown_types:
        print(f"Input: {spell} -> {cast_spell(spell)}")
    print()


if __name__ == "__main__":
    main()
