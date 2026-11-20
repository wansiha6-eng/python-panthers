class Player:
    def __init__(self, player_id, name, role, franchise, credits):
        self.player_id = player_id
        self.name = name
        self.role = role
        self.franchise = franchise
        self.credits = credits

    def __str__(self):
        return (
            f"{self.name} ({self.franchise}, "
            f"{self.role}, {self.credits} cr)"
        )


class FantasyTeam:
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
            if player.role not in counts:
                counts[player.role] = 0
            counts[player.role] += 1
        return counts

    def set_captain(self, captain, vice_captain):
        self.captain = captain
        self.vice_captain = vice_captain

    def __str__(self):
        size = len(self.players)
        cost = self.total_credits()
        return (
            f"{self.team_name} (owner: {self.owner}, "
            f"{size} players, {cost} cr)"
        )


farhan = Player(
    "P072", "Sahibzada Farhan", "Wicket-keeper", "Multan Sultans", 10.5
)

warner = Player(
    "P037", "DA Warner", "Batter", "Karachi Kings", 9.5
)

roy = Player(
    "P038", "JJ Roy", "Batter", "Karachi Kings", 9.0
)

hendricks = Player(
    "P039", "RR Hendricks", "Batter", "Karachi Kings", 10.0
)

rossouw = Player(
    "P108", "RR Rossouw", "Batter", "Quetta Gladiators", 7.0
)

saim = Player(
    "P012", "Saim Ayub", "All-rounder", "Hyderabad Kingsmen", 10.5
)

faheem = Player(
    "P027", "Faheem Ashraf", "All-rounder", "Islamabad United", 9.5
)

abbas = Player(
    "P045", "Abbas Afridi", "Bowler", "Karachi Kings", 10.0
)

hasan = Player(
    "P046", "Hasan Ali", "Bowler", "Karachi Kings", 10.0
)

sufiyan = Player(
    "P101", "Sufiyan Muqeem", "Bowler", "Peshawar Zalmi", 6.5
)

faisal = Player(
    "P079", "Faisal Akram", "Bowler", "Multan Sultans", 7.0
)


team = FantasyTeam("Python Panthers", "Wanisha")

for player in [
    farhan, warner, roy, hendricks, rossouw, saim,
    faheem, abbas, hasan, sufiyan, faisal
]:
    team.add_player(player)

team.set_captain(saim, faheem)

print(team)

print("\nPlayers:")
for player in team.players:
    print(player)

print("\nTotal players:", len(team.players))
print("Total credits:", team.total_credits())
print("Players by role:", team.count_by_role())
print("Captain:", team.captain.name)
print("Vice-captain:", team.vice_captain.name)
