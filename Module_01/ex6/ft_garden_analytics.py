class Plant:

    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):

    def __init__(self, name: str, height: int, flower_color: str) -> None:
        super().__init__(name, height)
        self.flower_color = flower_color
        self.blooming = True

    def __str__(self) -> str:
        status = "blooming" if self.blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.flower_color} " \
               f"flowers ({status})"


class PrizeFlower(FloweringPlant):

    def __init__(
        self,
        name: str,
        height: int,
        flower_color: str,
        prize_points: int,
    ) -> None:
        super().__init__(name, height, flower_color)
        self.prize_points = prize_points

    def __str__(self) -> str:
        status = "blooming" if self.blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.flower_color} " \
               f"flowers ({status}), Prize points: {self.prize_points}"


class GardenManager:

    gardens_count = 0

    class GardenStats:

        def __init__(self) -> None:
            self.plants_added = 0
            self.total_growth = 0

        def record_plant_added(self) -> None:
            self.plants_added += 1

        def record_growth(self) -> None:
            self.total_growth += 1

    class Garden:

        def __init__(self, owner: str) -> None:
            self.owner = owner
            self.plants = []
            self.stats = GardenManager.GardenStats()

        def add_plant(self, plant: Plant) -> None:
            self.plants.append(plant)
            self.stats.record_plant_added()
            print(f"Added {plant.name} to {self.owner}'s garden")

        def grow_all_plants(self) -> None:
            print(f"{self.owner} is helping all plants grow...")
            for plant in self.plants:
                plant.grow()
                self.stats.record_growth()

        def get_score(self) -> int:
            score = 0
            for plant in self.plants:
                score += plant.height
            if self.plants:
                last_plant = self.plants[-1]
                if last_plant.__class__.__name__ == 'PrizeFlower':
                    score += last_plant.prize_points
            return score

        def print_report(self) -> None:
            print(f"\n=== {self.owner}'s Garden Report ===")
            print("Plants in garden:")
            for plant in self.plants:
                print(f"- {plant}")

            regular = 0
            flowering = 0
            prize = 0
            print("\n")
            for p in self.plants:
                if p.__class__.__name__ == 'Plant':
                    regular += 1
                elif p.__class__.__name__ == 'FloweringPlant':
                    flowering += 1
                elif p.__class__.__name__ == 'PrizeFlower':
                    prize += 1

            print(f"Plants added: {self.stats.plants_added}, Total growth:"
                  f" {self.stats.total_growth}cm")
            print(f"Plant types: {regular} regular, {flowering} flowering,"
                  f" {prize} prize flowers")

    def __init__(self) -> None:
        self.gardens = {}
        GardenManager.gardens_count += 1

    def create_garden(self, owner: str) -> 'GardenManager.Garden':
        garden = self.Garden(owner)
        self.gardens[owner] = garden
        return garden

    def get_garden_scores(self) -> dict:
        scores = {owner: garden.get_score() for owner,
                  garden in self.gardens.items()}
        return scores

    @classmethod
    def create_garden_network(cls) -> 'GardenManager':
        return cls()

    @staticmethod
    def validate_height(height: int) -> bool:
        return height > 0


def main() -> None:
    print("=== Garden Management System ===")

    manager = GardenManager.create_garden_network()

    alice_garden = manager.create_garden("Alice")
    alice_garden.add_plant(Plant("Oak Tree", 100))
    alice_garden.add_plant(FloweringPlant("Rose", 25, "red"))
    alice_garden.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

    alice_garden.grow_all_plants()

    alice_garden.print_report()

    print(f"Height validation test: {GardenManager.validate_height(100)}")

    bob_garden = manager.create_garden("Bob")
    bob_garden.add_plant(Plant("Maple", 80))

    scores = manager.get_garden_scores()
    print(f"Garden scores - Alice: {scores['Alice']}, Bob: {scores['Bob']}")

    print(f"Total gardens managed: {GardenManager.gardens_count}")


if __name__ == "__main__":
    main()
