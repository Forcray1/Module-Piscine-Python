class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def afficher(self) -> None:
        print(f"{self.name:15} | {self.height:>8}cm | {self.age:>10} days old")


class Factory:
    def __init__(self) -> None:
        self.plants = []

    def Add_Plant(self, name: str, height: int, age: int) -> Plant:
        plante = Plant(name, height, age)
        self.plants.append(plante)
        print(f"Plant Created: {name}")
        return plante

    def Add_Multiple(self, data_list: list) -> None:
        for plant in data_list:
            self.Add_Plant(**plant)

    def Afficher_inventaire(self) -> None:
        print("=== Plant Factory Output ===")
        print(f"{'Nom':15} | {'Hauteur':>8} | {'Âge':>12}")
        for plante in self.plants:
            plante.afficher()


def main() -> None:
    factory = Factory()

    factory.Add_Plant("Rose", 25, 30)
    factory.Add_Plant("Tulipe", 15, 20)
    factory.Add_Plant("Orchidee", 30, 60)
    factory.Add_Plant("Marguerite", 20, 40)
    factory.Add_Plant("Oeillet", 35, 50)

    plantes_data = [
        {"name": "Cactus", "height": 50, "age": 365},
        {"name": "Bambou", "height": 120, "age": 180},
        {"name": "Fougere", "height": 40, "age": 90},
        {"name": "Lavande", "height": 35, "age": 45},
        {"name": "Acacia", "height": 235, "age": 1576}
    ]

    factory.Add_Multiple(plantes_data)

    factory.Afficher_inventaire()

    print(f"Total plants created: {len(factory.plants)}")


if __name__ == "__main__":
    main()
