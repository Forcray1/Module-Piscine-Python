import math
import sys


def parse_coords(raw: str) -> tuple:
    parts = [x.strip() for x in raw.split(",")]
    return tuple(int(x) for x in parts)


def distance(coords: tuple, coords2: tuple) -> float:
    x, y, z = coords
    x2, y2, z2 = coords2
    return math.sqrt((x - x2) ** 2 + (y - y2) ** 2 + (z - z2) ** 2)


def main() -> None:
    count = 0
    for _ in sys.argv:
        count += 1
    if count != 2:
        print("Usage: python3 ft_coordinate_system.py <x,y,z>")
        return
    print("=== Game Coordinate System ===\n")

    raw = sys.argv[1]
    try:
        coords = parse_coords(raw)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        return

    print(f"Position created: {coords}")
    ref_coords = (0, 1, 0)
    print(
        f"Distance between {ref_coords} and {coords}: "
        f"{distance(coords, ref_coords):.2f}\n"
    )

    print(f"Parsing coordinates: \"{raw}\"")
    print(f"Parsed position: {coords}")

    print("Unpacking demonstration:")
    x, y, z = coords
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
