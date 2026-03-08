from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        defense: int,
        health: int,
        mana: int,
        combat_type: str,
        max_mana: int = 10
    ):
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.defense = defense
        self.health = health
        self.mana = mana
        self.max_mana = max_mana
        self.combat_type = combat_type

    def play(self, game_state: dict) -> dict:
        available_mana = game_state.get("available_mana", 0)
        if not self.is_playable(available_mana):
            return {
                "played": False,
                "reason": "Not enough mana",
                "required": self.cost,
                "available": available_mana,
            }
        return {
            "played": True,
            "card": self.name
        }

    def attack(self, target: str) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": self.combat_type
        }

    def defend(self, incoming_damage: int) -> dict:
        if incoming_damage < self.health:
            damage_taken = incoming_damage - self.defense
            self.health = self.health - damage_taken
            alive = True
        else:
            alive = False
            self.health = 0
            damage_taken = incoming_damage - self.defense
        return {
            "defender": self.name,
            "damage taken": incoming_damage - self.defense,
            "damaged blocked": incoming_damage - damage_taken,
            "still_alive": alive,
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack_power": self.attack_power,
            "defense": self.defense,
            "health": self.health,
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        if self.mana <= 0:
            return {"action": "cast_spell", "success": False,
                    "reason": "No mana"}
        self.mana -= 4
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": 4
        }

    def channel_mana(self, amount: int) -> dict:
        amount = amount
        self.mana = self.mana + amount
        return {"channeled": amount, "total_mana": self.mana + amount}

    def get_magic_stats(self) -> dict:
        return {"mana": self.mana, "max_mana": self.max_mana}
