from player_reader import PlayerReader
from rich.table import Table

class PlayerStats:
    def __init__(self, players):
        self.players = players.get_players()

    def top_scorers_by_nationality(self, nat, season):
        table = Table(title=f"Top scorers of {nat} season {season}")
        table.add_column("name",style="cyan")
        table.add_column("team",style="magenta")
        table.add_column("goals",style="green")
        table.add_column("assists",style="green")
        table.add_column("points",style="green")
        self.players.sort(key=lambda x: x.points, reverse=True)
        print(f"Players from {nat}\n")
        for player in self.players:
            if player.nationality == nat:
                table.add_row(str(player.name), str(player.team), str(player.goals), str(player.assists), str(player.points))
        return table
        
        
