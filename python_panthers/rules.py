TEAM_SIZE = 11
MAX_CREDITS = 100
MAX_FROM_ONE_FRANCHISE = 7

ROLE_NAMES = {
    "WK": "Wicket-keeper",
    "BAT": "Batter",
    "AR": "All-rounder",
    "BOWL": "Bowler",
}

ROLE_LIMITS = {
    "Wicket-keeper": (1, 2),
    "Batter": (3, 5),
    "All-rounder": (1, 3),
    "Bowler": (3, 5),
}


def check_players_count(team):
    count = len(team.players)
    if count != TEAM_SIZE:
        return [f"Team must have {TEAM_SIZE} players, but has {count}"]
    return []


def check_budget(team):
    total = team.total_credits()
    if total > MAX_CREDITS:
        return [f"Team has {total} credits, but maximum is {MAX_CREDITS}"]
    return []


def check_franchise_limit(team):
    errors = []
    for franchise, count in team.count_by_franchise().items():
        if count > MAX_FROM_ONE_FRANCHISE:
            errors.append(
                f"Team has {count} players from {franchise}, "
                f"but maximum is {MAX_FROM_ONE_FRANCHISE}"
            )
    return errors


def check_roles(team):
    counts = team.count_by_role()
    errors = []
    for role, (low, high) in ROLE_LIMITS.items():
        count = counts.get(role, 0)
        if count < low or count > high:
            errors.append(
                f"Team has {count} players with role {role}, "
                f"but must have between {low} and {high}"
            )
    for role in counts:
        if role not in ROLE_LIMITS:
            errors.append(f"Unknown player role: {role}")
    return errors


def check_captains(team):
    if team.captain is None or team.vice_captain is None:
        return ["Team must have both a captain and a vice-captain"]

    errors = []
    if team.captain not in team.players:
        errors.append(f"Captain {team.captain.name} is not in the team")
    if team.vice_captain not in team.players:
        errors.append(f"Vice-captain {team.vice_captain.name} is not in the team")
    if team.captain == team.vice_captain:
        errors.append("Captain and vice-captain cannot be the same player")
    return errors
