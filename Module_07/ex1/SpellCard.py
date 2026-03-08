from ex0.Card import Card


class SpellCard(Card):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            effect_type: str
    ):
        super().__init__(name, cost, rarity)
        if not isinstance(effect_type, str) or not effect_type.strip():
            raise ValueError("effect_type must be a non-empty string")
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        game_state = game_state
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect_type
        }

    def resolve_effect(self, targets: list) -> dict:
        return {
            "spell": self.name,
            "target": targets,
            "effect_resolved": True
        }
