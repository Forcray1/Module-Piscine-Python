import alchemy


def main() -> None:
    print("=== Sacred Scroll Mastery ===\n")
    print("Testing direct module access:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print(f"alchemy.elements.create_water():"
          f" {alchemy.elements.create_water()}")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print(f"alchemy.elements.create_water():"
          f" {alchemy.elements.create_water()}")

    print("\nTesting package-level access (controlled by __init__.py):")
    try:
        print(f"alchemy.create_fire():  {alchemy.create_fire()}")
    except AttributeError:
        print("create_fire() is not accessible")
    try:
        print(f"alchemy.create_water(): {alchemy.create_water()}")
    except AttributeError:
        print("create_water() is not accessible")
    try:
        print(f"alchemy.create_earth(): "
              f"{alchemy.create_earth()}")
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")
    try:
        print(f"alchemy.create_air(): "
              f"{alchemy.create_air()}")
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")
    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
