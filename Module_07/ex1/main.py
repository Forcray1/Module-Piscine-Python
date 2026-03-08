from ex0.CreatureCard import CreatureCard
from ex1.Deck import Deck
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


def main() -> None:
    print("=== DataDeck Deck Builder ===")
    print()
    print("Building deck with different card types...")
    deck = Deck()
    lightning_bolt = SpellCard("Lightning Bolt", 3, "Common",
                               "damage")
    mana_crystal = ArtifactCard("Mana Crystal", 2, "Common", 10,
                                "Permanent: +1 mana per turn")
    fire_dragon = CreatureCard("Fire Dragon", 5, "Rare", 4, 4)
    deck.add_card(lightning_bolt)
    deck.add_card(mana_crystal)
    deck.add_card(fire_dragon)
    stats = deck.get_deck_stats()
    print(f"Deck stats: {stats}\n")
    print("Drawing and playing cards:\n")
    card_types = {
        "SpellCard": "Spell",
        "ArtifactCard": "Artifact",
        "CreatureCard": "Creature"
    }

    def get_type_str(card):
        return card_types.get(card.__class__.__name__, "Card")
    for _ in range(3):
        card = deck.draw_card()
        if card:
            type_str = get_type_str(card)
            print(f"Drew: {card.name} ({type_str})")
            play_result = card.play({})
            print(f"Play result: {play_result}")
            print()
    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
