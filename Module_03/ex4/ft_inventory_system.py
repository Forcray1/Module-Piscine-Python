import sys


def ft_int(s: str) -> int:
    res = 0
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
              '7': 7, '8': 8, '9': 9}
    if s == "":
        raise ValueError("empty value")
    for x in s:
        if x not in digits:
            raise ValueError(f"invalid integer: {s}")
        res = res * 10 + digits[x]
    return res


def main() -> None:
    inventory = dict()
    for input in sys.argv[1:]:
        if ":" not in input:
            continue
        name = input.split(":")[0]
        value = input.split(":")[1]
        try:
            quantity = ft_int(value)
        except ValueError:
            print("quantity must be a int")
            return
        inventory[name] = quantity
    if inventory == dict():
        print("enter some stuff with this format: item:quantity")
        return
    Total_items = 0
    Unique_items = 0
    for qty in inventory.values():
        Total_items += qty
        Unique_items += 1
    print("=== Inventory System Analysis ===\n")
    print(f"Total items in inventory: {Total_items}")
    print(f"Unique item types: {Unique_items}")
    print("\n=== Current Inventory ===\n")
    for x in inventory.items():
        percentage = x[1] / Total_items * 100
        print(f"{x[0]}: {x[1]} units ({percentage:.1f}%)")
    print("\n=== Inventory Statistics ===\n")
    most = 0
    most_name = 0
    for x in inventory.items():
        most = x[1]
        most_name = x[0]
        break
    less = 0
    less_name = 0
    for x in inventory.items():
        less = x[1]
        less_name = x[0]
        break
    for x in inventory.items():
        if x[1] > most:
            most = x[1]
            most_name = x[0]
        else:
            pass
    print(f"Most abundant: {most_name} ({most} units)")
    for x in inventory.items():
        if x[1] < less:
            less = x[1]
            less_name = x[0]
        else:
            pass
    print(f"Least abundant: {less_name} ({less} units)")
    print("\n=== Item Categories ===\n")
    moderate = dict()
    scarce = dict()
    for x in inventory.items():
        if x[1] <= 3:
            scarce[x[0]] = x[1]
        else:
            moderate[x[0]] = x[1]
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")
    print("\n=== Management Suggestions ===\n")
    restock = dict()
    for x in inventory.items():
        if x[1] == 1:
            restock[x[0]] = x[1]
        else:
            pass
    print(f"Restock needed: {restock}")
    print("\n=== Dictionary Properties Demo ===\n")
    keys = []
    for x in inventory.items():
        keys.append(x[0])
    print(f"Dictionary keys: {keys}")
    values = []
    for x in inventory.items():
        values.append(x[1])
    print(f"Dictionary values: {values}")
    item = "Sword"
    indict = False
    for x in inventory.items():
        if x[0] == item:
            indict = True
            break
        else:
            pass
    print(f"Sample lookup - {item} in inventory: {indict}")


if __name__ == "__main__":
    main()
