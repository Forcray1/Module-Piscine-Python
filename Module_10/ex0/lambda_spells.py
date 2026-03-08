def artifact_sorter(artifacts: list[dict],) -> list[dict]:
    sort = sorted(artifacts, key=lambda artifact: artifact['power'],
                  reverse=True)
    return sort


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    mage = list(filter(lambda mage: mage['power'] >= min_power, mages))
    return mage


def spell_transformer(spells: list[str]) -> list[str]:
    str_mod = list(map(lambda spell: f"* {spell} *", spells))
    return str_mod


def mage_stats(mages: list[dict]) -> dict:
    mage_stats = {}
    max_power = max(mages, key=lambda mage: mage['power'])
    min_power = min(mages, key=lambda mage: mage['power'])
    mage_stats['max'] = max_power
    mage_stats['min'] = min_power
    powers = list(map(lambda mage: mage['power'], mages))
    avg_power = sum(powers) / len(powers)
    mage_stats['avg_power'] = avg_power
    return mage_stats


def main():
    print("\nTesting artifact sorter...")
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85},
        {'name': 'Fire Staff', 'power': 92}
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    print(f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']}"
          f" power) comes before {sorted_artifacts[1]['name']} "
          f"({sorted_artifacts[1]['power']} power)")

    print("\nTesting spell transformer...")
    spells = ['fireball', 'heal', 'shield']
    transformed = spell_transformer(spells)
    print(' '.join(transformed))


if __name__ == "__main__":
    main()
