class SecurePlant:
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
        print(f"{self.name:15} | {self.__height:>8}cm | {self.__age:>10}"
              f" days old")


def main() -> None:
    print("=== valid plant ===")
    plant1 = SecurePlant("Rose", 25, 30)
    print()

    print("=== Displaying plant ===")
    plant1.afficher()
    print()

    print("=== Valid height update ===")
    plant1.set_height(50)
    print()

    print("=== Invalid height update (negative) ===")
    plant1.set_height(-10)
    print()

    print("=== Valid age update ===")
    plant1.set_age(45)
    print()

    print("=== Invalid age update (negative) ===")
    plant1.set_age(-5)
    print()

    print("=== Accessing data safely ===")
    print(f"Height: {plant1.get_height()}cm")
    print(f"Age: {plant1.get_age()} days")
    print()

    print("=== Creating plant with invalid initial values ===")
    plant2 = SecurePlant("Tulipe", -15, -20)
    plant2.afficher()
    print()

    print("=== FINAL STATE ===")
    plant1.afficher()


if __name__ == "__main__":
    main()
