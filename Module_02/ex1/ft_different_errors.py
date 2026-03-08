def trigger_value_error(value_str: str) -> None:
    int(value_str)


def trigger_zero_division(divisor: int) -> None:
    _ = 10 / divisor


def trigger_file_not_found(filename: str) -> None:
    open(filename, "r")


def trigger_key_error(data: dict, key: str) -> None:
    _ = data[key]


def garden_operations(
    operation: str,
    value_str: str = "abc",
    divisor: int = 0,
    filename: str = "missing.txt",
    data: dict | None = None,
    key: str = "missing_plant",
) -> None:
    if data is None:
        data = {"plants": 5}

    if operation == "value":
        try:
            trigger_value_error(value_str)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
    elif operation in {"zero", "zero_division"}:
        try:
            trigger_zero_division(divisor)
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
    elif operation == "file":
        try:
            trigger_file_not_found(filename)
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
    elif operation == "key":
        try:
            trigger_key_error(data, key)
        except KeyError as e:
            print(f"Caught KeyError: {e}")
    else:
        print(f"Unknown operation: {operation}")


def test_error_types(
    value_str: str,
    divisor: int,
    filename: str,
    data: dict,
    key: str,
) -> None:
    print("=== Garden Error Types Demo ===")
    print("\nTesting ValueError...")
    try:
        trigger_value_error(value_str)
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("\nTesting ZeroDivisionError...")
    try:
        trigger_zero_division(divisor)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("\nTesting FileNotFoundError...")
    try:
        trigger_file_not_found(filename)
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

    print("\nTesting KeyError...")
    try:
        trigger_key_error(data, key)
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    print("\nTesting multiple errors together...")
    try:
        trigger_value_error(value_str)
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")
    try:
        trigger_zero_division(divisor)
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    value_str = "abc"
    divisor = 0
    filename = "missing.txt"
    data = {"plants": 5}
    key = "missing_plant"

    test_error_types(value_str, divisor, filename, data, key)
