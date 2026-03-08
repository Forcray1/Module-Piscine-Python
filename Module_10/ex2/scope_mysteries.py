from typing import Callable


def mage_counter() -> Callable:
    count = 0

    def wrapper():
        nonlocal count
        count += 1
        return count
    return wrapper


def spell_accumulator(initial_power: int) -> Callable:
    power = 0

    def wrapper():
        nonlocal power
        power += initial_power
        return power
    return wrapper


def enchantment_factory(enchantment_type: str) -> Callable:
    item = "sword"

    def wrapper():
        nonlocal item
        item = enchantment_type + " " + item
        return item
    return wrapper


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value) -> str:
        nonlocal memory
        memory[key] = value
        return f"Stored '{key}' successfully"

    def recall(key: str):
        if key in memory:
            return memory[key]
        else:
            return "Memory not found"
    return {
        'store': store,
        'recall': recall
    }


def main() -> None:
    count = mage_counter()
    print("Testing mage counter...")
    print(f"Call1: {count()}")
    print(f"Call2: {count()}")
    print(f"Call3: {count()}")
    power = spell_accumulator(5)
    print("\nTesting spell accumulator...")
    print(f"Call1: {power()}")
    print(f"Call2: {power()}")
    print(f"Call3: {power()}")
    print("\nTesting enchantment factory...")
    enchanted_item = enchantment_factory("Flaming")
    print(f"{enchanted_item()}")
    enchanted_item = enchantment_factory("Frozen")
    print(f"{enchanted_item()}")
    print("\nTesting memory vault...")
    vault1 = memory_vault()
    vault2 = memory_vault()
    vault1['store']("1", "345")
    vault2['store']("1", "900")
    print(vault1['recall']("1"))
    print(vault2['recall']("1"))


if __name__ == "__main__":
    main()
