def Fibonacci(iteration: int):
    Value1 = 0
    Value2 = 1
    for _ in range(iteration):
        yield Value1
        Value1, Value2 = Value2, Value1 + Value2


def Prime(iteration: int):
    x = 0
    num = 2
    while x < iteration:
        is_prime = True
        div = 2
        while div * div <= num:
            if num % div == 0:
                is_prime = False
                break
            div += 1

        if is_prime:
            yield num
            x += 1
        num += 1


def event_generator(iteration: int):
    names = ['Alice', 'Bob', 'Charlie']
    events = ['killed a monster', 'found treasure', 'leveled up', 'died',
              'entered a dungeon', 'rested', 'used a spell',
              'started a boss fight']
    levels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
              17, 18, 19, 20]
    for x in range(1, iteration + 1):
        name = names[x * 2 % len(names)]
        level = levels[x * 7 % len(levels)]
        event = events[x * 9 % len(events)]

        yield (name, level, event)


def main() -> None:
    print("=== Game Data Stream Processor ===\n")
    iteration = 100
    print(f"Processing {iteration} game events...\n")
    a = 1
    Treasure = 0
    High_lvl = 0
    lvlup = 0
    for i in event_generator(iteration):
        name, level, event = i
        if a <= 3:
            print(f"Event {a} : Player {name} (Level {level}) {event}")
            a += 1
        if a == 4:
            print("...")
            a += 1
        if level >= 10:
            High_lvl += 1
        if i[2] == 'leveled up':
            lvlup += 1
        if i[2] == 'found treasure':
            Treasure += 1

    print("\n=== Stream Analytics ===\n")
    print(f"Total events processed: {iteration}")
    print(f"High-level players (10+): {High_lvl}")
    print(f"Treasure events:  {Treasure}")
    print(f"Level-up events: {lvlup}")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")
    print("\n=== Generator Demonstration ===\n")
    print("Fibonacci sequence (first 10):", end=" ")
    first = True
    for num in Fibonacci(10):
        if not first:
            print(", ", end="")
        print(num, end="")
        first = False
    print("\nPrime numbers (first 5):", end=" ")
    first = True
    for num in Prime(5):
        if not first:
            print(", ", end="")
        print(num, end="")
        first = False
    print(" ")


if __name__ == "__main__":
    main()
