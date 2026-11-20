import csv

from models import FantasyTeam, Player


def load_player(path):
    """Read a player CSV and return the players indexed by ID."""
    players = {}
    with open(path, newline="", encoding="utf-8-sig") as file:
        for row in csv.DictReader(file):
            player = Player.from_row(row)
            players[player.player_id] = player
    return players


def team_from_row(row, players):
    team = FantasyTeam(row["team_name"], row["owner"])
    for player_id in row["players"].split(";"):
        team.add_player(players[player_id.strip()])

    team.set_captain(
        players[row["captain"].strip()],
        players[row["vice_captain"].strip()],
    )
    return team


def load_team(path, players):
    """Return the first team in a team CSV, or None if it has no rows."""
    with open(path, newline="", encoding="utf-8-sig") as file:
        for row in csv.DictReader(file):
            return team_from_row(row, players)
    return None


def load_teams(path, players):
    """Return every team in a team CSV."""
    with open(path, newline="", encoding="utf-8-sig") as file:
        return [team_from_row(row, players) for row in csv.DictReader(file)]
