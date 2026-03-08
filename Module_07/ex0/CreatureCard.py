from .Card import Card


class CreatureCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int
    ):
        super().__init__(name, cost, rarity)
        try:
            if attack >= 0:
                self.attack = attack
            else:
                raise ValueError("attack must be a positive int")
            if health > 0:
                self.health = health
            else:
                raise ValueError("Health must be a non null positive int")

        except ValueError as e:
            raise ValueError(f"Error : {e}")

    def play(self, game_state: dict) -> dict:
        game_state = game_state
        return {"card_played": self.name, "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"}

    def get_card_info(self) -> dict:
        return super().get_card_info() | {"type": "Creature",
                                          "attack": self.attack,
                                          "health": self.health}

    def attack_target(self, target: str, mana: int) -> dict:
        if mana > self.cost:
            return {"attacker": self.name, "target": target, "damage_dealt":
                    self.attack, "combat_resolved": True}
        else:
            return {"attacker": self.name, "target": target, "damage_dealt":
                    self.attack, "combat_resolved": False}
