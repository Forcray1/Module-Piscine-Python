def main() -> None:
    Alice = {
        'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'
    }
    Bob = {
        'first_kill', 'level_10', 'boss_slayer', 'collector'
    }
    Charlie = {
        'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
        'perfectionist'
    }
    print("=== Achievement Tracker System ===\n")
    print(f"Player Alice achievments : {Alice}")
    print(f"Player Bob achievments : {Bob}")
    print(f"Player Charlie achievments : {Charlie}")
    print("\n=== Achievement Analytics ===\n")
    uniques = Alice | Bob | Charlie
    print(f"All unique achievements: {uniques}")
    print(f"Total unique achievements: {len(uniques)}")
    common = Alice & Bob & Charlie
    print(f"\nCommon to all players:  {common}")
    rare = ((Alice - Bob - Charlie) | (Bob - Alice - Charlie) |
            (Charlie - Alice - Bob))
    print(f"Rare achievements (1 player): {rare}")
    AvB = Alice & Bob
    print(f"\nAlice vs Bob common: {AvB}")
    A_uniques = Alice - Bob
    print(f"Alice unique: {A_uniques}")
    B_uniques = Bob - Alice
    print(f"Bob unique: {B_uniques}")


if __name__ == "__main__":
    main()
