import sys


def main() -> None:
    i = 0

    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print("No arguments provided!")
        print(f"Program name: {(sys.argv[0]).split("/")[-1]}")
        print("Total arguments: 1")
    else:
        print(f"Program name: {(sys.argv[i]).split("/")[-1]}")
        i += 1
        print(f"Arguments received: {len(sys.argv) - 1}")
        while i < len(sys.argv):
            print(f"argument {i} : {sys.argv[i]}")
            i += 1
        print(f"Total arguments: {i}")


if __name__ == "__main__":
    main()
