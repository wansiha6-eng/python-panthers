from pathlib import Path

from loader import load_player, load_team
from rules import MAX_FROM_ONE_FRANCHISE


def main():
    data_dir = Path(__file__).resolve().parent / "data"
    players = load_player(data_dir / "players.csv")
    team = load_team(data_dir / "my_team.csv", players)
    if team is None:
        print("No team found in my_team.csv.")
        return 1

    print(team)
    errors = team.check_rules()
    if errors:
        for error in errors:
            print(error)
        return 1

    franchise_counts = team.count_by_franchise()
    franchise = max(franchise_counts, key=franchise_counts.get)
    print(
        f"Largest franchise group: {franchise} - {franchise_counts[franchise]} "
        f"players (limit: {MAX_FROM_ONE_FRANCHISE})."
    )
    print("All team selection rules met.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
