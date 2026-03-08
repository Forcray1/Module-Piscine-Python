def ft_plant_age() -> None:
    print("Enter plant age in days:")
    age = int(input())
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
    return
