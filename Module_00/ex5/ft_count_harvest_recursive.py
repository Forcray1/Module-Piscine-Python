def recursive(days: int) -> None:
    if days > 0:
        recursive(days - 1)
    print(f"Day {days}")
    days = days + 1
    return


def ft_count_harvest_recursive() -> None:
    print("Days until harvest: ")
    days = int(input())
    recursive(days)
    print("Harvest time!")
