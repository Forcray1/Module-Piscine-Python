def check_temperature(temp_str: str) -> int:
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return 0

    if 0 <= temp <= 40:
        print(f"Temperature {temp}°C is perfect for plants!")
    elif temp > 40:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)")
    else:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)")
    return temp


def main() -> None:
    print("=== Garden Temperature Checker ===")
    print("\nTesting temperature: 25")
    temp = ("25")
    check_temperature(temp)
    print("\nTesting temperature: abc")
    temp = ("abc")
    check_temperature(temp)
    print("\nTesting temperature: 100")
    temp = ("100")
    check_temperature(temp)
    print("\nTesting temperature: -50")
    temp = ("-50")
    check_temperature(temp)
    print("\nAll tests completed - program didn't crash!")
    return


if __name__ == "__main__":
    main()
