from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.console import Console

def main():
    console = Console()
    season = input("Select season: ")
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    while True:
        nationality = input("Select nationality: ")
        players = stats.top_scorers_by_nationality(nationality,season)
        console.print(players)


main()