def ft_water_reminder() -> None:
    print("Days since last watering:")
    day = int(input())
    if day > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
    return
