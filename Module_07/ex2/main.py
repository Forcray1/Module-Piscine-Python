from ex0.Card import Card
from ex2.EliteCard import EliteCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical


def main() -> None:
    print("=== DataDeck Ability System ===\n")
    print("EliteCard capabilities:")
    card_methods = [
        method for method in dir(Card)
        if callable(getattr(Card, method)) and not method.startswith("__")
    ]
    combatable_methods = [
        method for method in dir(Combatable)
        if (callable(getattr(Combatable, method)) and
            not method.startswith("__"))
    ]
    magical_methods = [
        method for method in dir(Magical)
        if callable(getattr(Magical, method)) and not method.startswith("__")
    ]
    print(f"- Card: {card_methods}")
    print(f"- Combatable: {combatable_methods}")
    print(f"- Magical: {magical_methods}")
    print("\nPlaying Arcane Warrior (Elite Card):\n")
    print("Combat phase:")
    elite = EliteCard("Arcane warrior", 1, "Epic", 5, 3, 10, 5, "melee")
    print(f"Attack result: {elite.attack("Enemy")}")
    print(f"Defense result: {elite.defend(5)}")
    print("\nMagic phase:")
    print(f"Spell cast: {elite.cast_spell("Fireball",
                                          ["Enemy 1", "Enemy 2"])}")
    print(f"Mana channel: {elite.channel_mana(3)}")
    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
