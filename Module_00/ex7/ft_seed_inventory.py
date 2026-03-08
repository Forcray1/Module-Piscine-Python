def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type2 = seed_type.capitalize()
    if unit == "packets":
        print(f"{seed_type2} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed_type2} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{seed_type2} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
    return
