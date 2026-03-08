from .CreatureCard import CreatureCard


def main():
    dragon = CreatureCard(name="Fire Dragon", cost=5, rarity='Legendary',
                          attack=7, health=5)

    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:")
    print(f"\nCreatureCard Info:\n{dragon.get_card_info()}")
    print(f"\nPlaying Fire Dragon with 6 mana available:\n"
          f"Playable: {dragon.is_playable(6)}")
    a = dict()
    print(f"Play result: {dragon.play(a)}")
    print(f"\nFire Dragon attacks Goblin Warrior:\n"
          f"Attack result: {dragon.attack_target("Goblin Warrior", 6)}")
    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {dragon.is_playable(3)}")
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
