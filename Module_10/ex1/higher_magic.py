from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(*args, **kwargs):
        result1 = spell1(*args, **kwargs)
        result2 = spell2(*args, **kwargs)
        return (result1, result2)
    return combined_spell


def spell1() -> str:
    return "Fireball hits Dragon"


def spell2() -> str:
    return "Heals Dragon"


def power_amplifier(
        base_spell: Callable,
        multiplier: int
        ) -> Callable:
    def amplfier(*args, **kwargs):
        result = base_spell(*args, **kwargs) * multiplier
        return result
    return amplfier


def fireball() -> int:
    return 1


def conditional_caster(condition: Callable,
                       spell: Callable
                       ) -> Callable:
    def valid(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled"
    return valid


def spell(mana_cost: int) -> str:
    return f"spell casted ({mana_cost} mana used)"


def enough_mana(mana_cost: int, mana_pool: int) -> bool:
    if mana_cost <= mana_pool:
        return True
    else:
        return False


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(*args, **kwargs):
        list_spells = list()
        for i in spells:
            list_spells.append(i(*args, **kwargs))
        return list_spells
    return sequence


def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(spell1, spell2)
    results = combined()
    print(f"Combined spell result : {', '.join(results)}")
    spell_amplified = power_amplifier(fireball, 3)
    print("\nTesting power amplifier...")
    print(f"Original: {fireball()}, Amplified: {spell_amplified()}")
    spell_cost = 3
    mana_pool = 10
    castable = conditional_caster(lambda: enough_mana(spell_cost, mana_pool),
                                  lambda: spell(spell_cost))
    print("\nTesting conditional caster...")
    print(castable())
    spell_list = [lambda: spell1(), lambda: spell2()]
    sequence_spell = spell_sequence(spell_list)
    print("\nTesting spell sequence...")
    print(sequence_spell())


if __name__ == "__main__":
    main()
