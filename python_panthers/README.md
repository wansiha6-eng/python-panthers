# Python Panthers

Wanisha’s fantasy XI for the Advanced Python for AI Dugout League, PSL 2026.

## Run the project

Extract the ZIP, open the `python_panthers` folder in VS Code, and run these commands in the terminal.

```sh
python wanisha_python_panthers.py
python scratch.py
```

The first command runs the standalone assignment program from pages 2–4 of the PDF. The second loads the CSV roster and checks the selection rules. Both scripts use Python 3 and its standard library.

| Team detail | Value |
|---|---|
| Players | 11 |
| Credits | 99.5 out of 100 |
| Roles | 1 wicket-keeper, 4 batters, 2 all-rounders, 4 bowlers |
| Largest franchise group | Karachi Kings, 5 players out of the 7 allowed |
| Captain | Saim Ayub (`P012`), 2× points |
| Vice-captain | Faheem Ashraf (`P027`), 1.5× points |

## Project files

| File | Purpose |
|---|---|
| `wanisha_python_panthers.py` | Standalone assignment script |
| `models.py` | Reusable `Player`, `FantasyTeam`, and `League` classes |
| `loader.py` | CSV readers for players and teams |
| `rules.py` | Squad size, credit budget, franchise, role, and captain checks |
| `scratch.py` | Runs the CSV roster through the rule checks |
| `data/players.csv` | The 11 players listed in the PDF |
| `data/my_team.csv` | Roster order and captain selections |
| `.gitignore` | Excludes Python cache files and local environments |
| `GITHUB_GUIDE.md` | Setup, first push, troubleshooting, and future updates |

Follow the guide to publish the project from your own GitHub account. [GitHub guide](GITHUB_GUIDE.md)
