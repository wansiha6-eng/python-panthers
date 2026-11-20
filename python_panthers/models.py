from rules import (
    ROLE_NAMES,
    check_budget,
    check_captains,
    check_franchise_limit,
    check_players_count,
    check_roles,
)


class Player:
    """One cricketer in the PSL player list."""

    def __init__(self, player_id, name, role, franchise, credits):
        self.player_id = player_id
        self.name = name
        self.role = ROLE_NAMES.get(role, role)
        self.franchise = franchise
        self.credits = credits

    @classmethod
    def from_row(cls, row):
        return cls(
            player_id=row["player_id"],
            name=row["name"],
            role=row["role"].strip(),
            franchise=row["franchise"],
            credits=float(row["credits"]),
        )

    def __str__(self):
        return f"{self.name} ({self.franchise}, {self.role}, {self.credits} cr)"


class FantasyTeam:
    """A fantasy XI picked by one owner."""

    def __init__(self, team_name, owner):
        self.team_name = team_name
        self.owner = owner
        self.players = []
        self.captain = None
        self.vice_captain = None

    def add_player(self, player):
        self.players.append(player)

    def total_credits(self):
        total = 0
        for player in self.players:
            total += player.credits
        return total

    def count_by_role(self):
        counts = {}
        for player in self.players:
            counts[player.role] = counts.get(player.role, 0) + 1
        return counts

    def set_captain(self, captain, vice_captain):
        self.captain = captain
        self.vice_captain = vice_captain

    def count_by_franchise(self):
        """Count the selected players from each franchise."""
        counts = {}
        for player in self.players:
            counts[player.franchise] = counts.get(player.franchise, 0) + 1
        return counts

    def check_rules(self):
        """Return a list of rule violations."""
        errors = []
        errors.extend(check_players_count(self))
        errors.extend(check_budget(self))
        errors.extend(check_franchise_limit(self))
        errors.extend(check_roles(self))
        errors.extend(check_captains(self))
        return errors

    def __str__(self):
        size = len(self.players)
        cost = self.total_credits()
        return f"{self.team_name} (owner: {self.owner}, {size} players, {cost} cr)"


class League:
    """A collection of fantasy teams indexed by owner."""

    def __init__(self, name):
        self.name = name
        self.teams = {}

    def add_team(self, team):
        self.teams[team.owner] = team

    def find_team(self, owner):
        return self.teams.get(owner)

    def legal_teams(self):
        return [team for team in self.teams.values() if not team.check_rules()]

    def rank_teams(self):
        """Return the teams sorted by total credits, lowest first."""
        return sorted(self.teams.values(), key=lambda team: team.total_credits())
