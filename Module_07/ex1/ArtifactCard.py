from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        durability: int,
        effect: str
    ):
        super().__init__(name, cost, rarity)
        try:
            if durability >= 0:
                self.durability = durability
            else:
                raise ValueError("Durability must be a positive int")
        except ValueError as e:
            return f"Error: {e}"
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        game_state = game_state
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect
        }

    def activate_ability(self) -> dict:
        if self.durability > 0:
            self.durability -= 1
            return {
                "artifact": self.name,
                "ability_activated": True,
                "remaining_durability": self.durability
            }
        else:
            return {
                "artifact": self.name,
                "ability_activated": False,
                "reason": "Artifact is broken"
            }
