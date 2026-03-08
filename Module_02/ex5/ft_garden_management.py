class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(
            self,
            name: str,
            water_level: int,
            sunlight_hours: int
    ) -> None:
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:
    MIN_WATER = 1
    MAX_WATER = 10
    MIN_SUN = 2
    MAX_SUN = 12

    def __init__(self, water_tank: int) -> None:
        self.plants = []
        self.water_tank = water_tank

    def add_plant(
        self,
        name: str,
        water_level: int,
        sunlight_hours: int,
    ) -> Plant:
        if not name.strip():
            raise PlantError("Plant name cannot be empty!")
        try:
            water_level = int(water_level)
        except Exception:
            raise PlantError("Water level must be an integer!")
        try:
            sunlight_hours = int(sunlight_hours)
        except Exception:
            raise PlantError("Sunlight hours must be an integer!")

        plant = Plant(name, water_level, sunlight_hours)
        self.plants.append(plant)
        print(f"Added {name} successfully")
        return plant

    def water_plants(self) -> None:
        try:
            if self.water_tank <= 0:
                raise GardenError("Not enough water in tank")
        except GardenError as exc:
            print(f"Caught GardenError: {exc}")
            return
        print("Opening watering system")
        try:
            if not self.plants:
                raise WaterError("No plants to water")
            for plant in self.plants:
                print(f"Watering {plant.name} - success")
                plant.water_level += 1
                self.water_tank -= 1
        except WaterError as exc:
            print(f"Caught WaterError: {exc}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant: Plant) -> None:
        if not plant.name.strip():
            raise PlantError("Plant name cannot be empty!")
        if plant.water_level < self.MIN_WATER:
            raise PlantError(
                f"Water level {plant.water_level} is too low "
                f"(min {self.MIN_WATER})"
            )
        if plant.water_level > self.MAX_WATER:
            raise PlantError(
                f"Water level {plant.water_level} is too high "
                f"(max {self.MAX_WATER})"
            )
        if plant.sunlight_hours < self.MIN_SUN:
            raise PlantError(
                f"Sunlight hours {plant.sunlight_hours} is too low "
                f"(min {self.MIN_SUN})"
            )
        if plant.sunlight_hours > self.MAX_SUN:
            raise PlantError(
                f"Sunlight hours {plant.sunlight_hours} is too high "
                f"(max {self.MAX_SUN})"
            )
        print(
            f"{plant.name}: healthy "
            f"(water: {plant.water_level}, sun: {plant.sunlight_hours})"
        )


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    manager = GardenManager(2)

    print("Adding plants to garden...")
    try:
        manager.add_plant("tomato", 5, 8)
        manager.add_plant("lettuce", 10, 6)
        manager.add_plant("", 5, 6)
    except PlantError as exc:
        print(f"Error adding plant: {exc}")

    print("\nWatering plants...")
    manager.water_plants()

    print("\nChecking plant health...")
    try:
        for plant in manager.plants:
            manager.check_plant_health(plant)
    except PlantError as exc:
        print(f"Error checking {plant.name}: {exc}")

    print("\nTesting error recovery...")
    manager.water_plants()
    print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
