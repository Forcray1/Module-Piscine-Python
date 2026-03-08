def water_plants(plant_list: list) -> None:
    try:
        for plant in plant_list:
            if (plant):
                print(f"watering {plant}")
            else:
                raise ValueError()
    except ValueError:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    print("Opening watering system")
    plant_list1 = [
        "tomato",
        "lettuce",
        "carrots"
    ]
    water_plants(plant_list1)
    plant_list2 = [
        "tomato",
        "",
        "lettuce"
    ]
    print("\nTesting with error...")
    print("Opening watering system")
    water_plants(plant_list2)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
