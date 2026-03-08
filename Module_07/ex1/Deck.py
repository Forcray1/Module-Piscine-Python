import random
from ex0.Card import Card


class Deck:
    def __init__(self) -> None:
        self.deck = []

    def add_card(self, card: Card) -> None:
        if isinstance(card, Card):
            self.deck.append(card)
        else:
            print("Error, you need to add a Card")

    def remove_card(self, card_name: str) -> bool:
        for i in self.deck:
            if i == card_name:
                del self.deck[i]
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        return self.deck.pop(0)

    def get_deck_stats(self) -> dict:
        creatures = 0
        spells = 0
        artifacts = 0
        total_cost = 0
        for card in self.deck:
            class_name = card.__class__.__name__
            if class_name == "CreatureCard":
                creatures += 1
            elif class_name == "SpellCard":
                spells += 1
            elif class_name == "ArtifactCard":
                artifacts += 1

            total_cost += card.cost
        total_cards = len(self.deck)
        avg_cost = total_cost / total_cards if total_cards > 0 else 0.0
        avg_cost = f"{avg_cost:.1f}"
        return {
            "total_cards": total_cards,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg_cost
        }
