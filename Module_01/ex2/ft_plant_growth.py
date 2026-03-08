class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self) -> None:
        self.age += 1
        self.height += 2


def main() -> None:
    i = 0

    plant1 = Plant("Rose", 25, 30)
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant1.get_info()
        print("\n")
        plant1.grow()
        i += 1


if __name__ == "__main__":
    main()
