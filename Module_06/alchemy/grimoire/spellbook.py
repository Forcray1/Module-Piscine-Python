import alchemy.grimoire.validator as valid


def record_spell(spell_name: str, ingredients: str) -> str:
    validation_result = valid.validate_ingredients(ingredients)
    if f"{ingredients} - INVALID" in validation_result:
        return f"Spell rejected: {spell_name} ({validation_result})"
    elif f"{ingredients} - VALID" in validation_result:
        return f"Spell recorded: {spell_name} ({validation_result})"
    else:
        return f"Spell recording error: {spell_name} ({validation_result})"
