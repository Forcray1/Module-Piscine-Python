import sys


def main() -> None:

    i = 1

    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return
    try:
        Score = [int(arg) for arg in sys.argv[1:]]
    except ValueError:
        print("Error: all arguments must be integers.")
        return
    print(f"Score processed: {Score}")
    print(f"Total players: {len(sys.argv) - 1}")
    i = 1
    Total = 0
    while i < len(sys.argv):
        Total += int(sys.argv[i])
        i += 1
    print(f"Total score: {Total}")
    print(f"Average score: {Total / (len(sys.argv) - 1)}")
    highest = 0
    i = 1
    while i < len(sys.argv):
        if int(sys.argv[i]) > highest:
            highest = int(sys.argv[i])
            i += 1
        else:
            i += 1
    print(f"High score: {highest}")
    lowest = int(sys.argv[1])
    i = 1
    while i < len(sys.argv):
        if int(sys.argv[i]) < lowest:
            lowest = int(sys.argv[i])
            i += 1
        else:
            i += 1
    print(f"Low score: {lowest}")
    print(f"Score range: {highest - lowest}")


if __name__ == "__main__":
    main()
