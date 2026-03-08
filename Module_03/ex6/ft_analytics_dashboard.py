class Player:
    def __init__(
        self,
        name: str,
        achievements: set,
        region: str,
        activity: str
    ) -> None:
        self.name = name
        self.score = len(achievements) * 500
        self.achievements = achievements
        self.region = region
        if activity == "offline":
            self.activity = False
        elif activity == "online":
            self.activity = True


def main() -> None:
    alice_achievements = {
        'first_kill', 'level_10', 'treasure_hunter', 'speed_demon',
        'beta_tester'
    }
    bob_achievements = {
        'first_kill', 'level_10', 'collector'
    }
    charlie_achievements = {
        'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
        'perfectionist'
    }
    diana_achievements = {
        'first_kill', 'level_10', 'boss_slayer', 'speed_demon',
        'explorer', 'beta_tester'
    }
    alice = Player("alice", alice_achievements, "north", "online")
    bob = Player("bob", bob_achievements, "east", "online")
    charlie = Player("charlie", charlie_achievements, "north", "online")
    diana = Player("diana", diana_achievements, "central", "offline")
    players = [
        ("alice", alice),
        ("bob", bob),
        ("charlie", charlie),
        ("diana", diana)
    ]
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===\n")
    high_scorer = []
    for x in players:
        if x[1].score >= 2000:
            high_scorer.append(x[1].name)
    print(f"High scorers (>2000): {high_scorer}")
    score_doubled = []
    for x in players:
        score_doubled.append(x[1].score * 2)
    print(f"Scores doubled: {score_doubled}")
    online = []
    for x in players:
        if x[1].activity is True:
            online.append(x[1].name)
    print(f"Active players: {online}")
    print("\n=== Dict Comprehension Examples ===\n")
    print("Player scores: ", end="")
    first = True
    for x in players:
        if not first:
            print(", ", end="")
        print(f"{x[1].name}: {x[1].score}", end="")
        first = False
    score_categories = {"high": 0, "medium": 0, "low": 0}
    for x in players:
        if x[1].score <= 1500:
            score_categories["low"] += 1
        elif x[1].score <= 2500:
            score_categories["medium"] += 1
        else:
            score_categories["high"] += 1
    print(f"\nScore categories: {score_categories}")
    print("Achievement counts: ", end="")
    first = True
    for x in players:
        if not first:
            print(", ", end="")
        print(f"{x[1].name}: {len(x[1].achievements)}", end="")
        first = False
    print("\n\n=== Set Comprehension Examples ===\n")
    unique_players = []
    for x in players:
        if x[1].name not in unique_players:
            unique_players.append(x[1].name)
    print(f"Unique players: {unique_players}")

    achievement_counts = {}
    for x in players:
        for achievement in x[1].achievements:
            if achievement in achievement_counts:
                achievement_counts[achievement] += 1
            else:
                achievement_counts[achievement] = 1

    uniques = []
    for achievement in achievement_counts:
        if achievement_counts[achievement] == 1:
            uniques.append(achievement)
    print(f"Unique achievements: {uniques}")

    active_regions = []
    for x in players:
        if x[1].activity is True and x[1].region not in active_regions:
            active_regions.append(x[1].region)
    print(f"Active regions: {active_regions}")
    print("\n=== Combined Analysis ===\n")
    print(f"Total players: {len(players)}")
    total_unique = len(achievement_counts)
    print(f"Total unique achievements: {total_unique}")
    total_score = 0
    for x in players:
        total_score += x[1].score
    average = total_score / len(players)
    print(f"Average score: {average:.1f}")
    best = 0
    holder = alice
    for x in players:
        if x[1].score > best:
            best = x[1].score
            holder = x[1]
    print(f"Top performer: {holder.name} ({holder.score} points,"
          f" {len(holder.achievements)} achievments)")


if __name__ == "__main__":
    main()
