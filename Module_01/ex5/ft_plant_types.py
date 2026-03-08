class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.__height = 0
        self.__age = 0

        self.set_height(height)
        self.set_age(age)

    def set_height(self, n: int) -> bool:
        if n < 0:
            print(f"Invalid operation attempted: height {n}cm [REJECTED]")
            print("Security: Negative height rejected")
            return False
        else:
            self.__height = n
            print(f"Height updated: {self.__height}cm [OK]")
            return True

    def set_age(self, n: int) -> bool:
        if n < 0:
            print(f"Invalid operation attempted: age {n} days [REJECTED]")
            print("Security: Negative age rejected")
            return False
        else:
            self.__age = n
            print(f"Age updated: {self.__age} days [OK]")
            return True

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def afficher(self) -> None:
        print(f"{self.name:15} | {self.__height:>8}cm | {self.__age:>10} "
              f"days old")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int)\
          -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade = self.produce_shade()

    def produce_shade(self) -> float:
        return (self.trunk_diameter * self.get_height()) / 100

    def afficher(self) -> None:
        print(f"{self.name} (Tree): {self.get_height()}cm, "
              f"{self.get_age()} days, {self.trunk_diameter}cm diameter")
        print(f"{self.name} provides {self.shade:.2f} square meters of shade")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> bool:
        if self.get_age() > 7:
            print(f"{self.name} is blooming beautifully!")
            return True
        else:
            print(f"{self.name} needs {7 - self.get_age()} more days to bloom")
            return False

    def afficher(self) -> None:
        print(f"{self.name} (Flower): {self.get_height()}cm, {self.get_age()}"
              f" days, {self.color} color")
        self.bloom()


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str)\
          -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = self.calculate_nutritional_value()

    def calculate_nutritional_value(self) -> str:
        if self.harvest_season == "spring":
            return "vitamin C"
        elif self.harvest_season == "summer":
            return "vitamin D"
        elif self.harvest_season == "autumn":
            return "calcium"
        elif self.harvest_season == "winter":
            return "iron"
        else:
            return "vitamin A"

    def afficher(self) -> None:
        print(f"{self.name} (Vegetable): {self.get_height()}cm, "
              f"{self.get_age()} days, {self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")


def main() -> None:

    print("\n=== Creating Trees ===\n")
    oak = Tree("Oak", 500, 3650, 80)
    pine = Tree("Pine", 800, 5475, 60)

    print("\n=== Creating Flowers ===\n")
    rose = Flower("Rose", 25, 10, "Red")
    tulip = Flower("Tulip", 15, 5, "Yellow")

    print("\n=== Creating Vegetables ===\n")
    tomato = Vegetable("Tomato", 50, 80, "summer")
    carrot = Vegetable("Carrot", 20, 70, "autumn")

    print("\nTREES:\n")
    oak.afficher()
    print()
    pine.afficher()

    print("\nFLOWERS:\n")
    rose.afficher()
    print()
    tulip.afficher()

    print("\nVEGETABLES:\n")
    tomato.afficher()
    print()
    carrot.afficher()

    print("\n" + "=" * 80)


if __name__ == "__main__":
    main()
