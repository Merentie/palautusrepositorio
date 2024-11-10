from player_reader import PlayerReader


class PlayerStats:
    def __init__(self, players):
        self.players = players.get_players()

    def top_scorers_by_nationality(self, nat):
        lista = []
        self.players.sort(key=lambda x: x.points, reverse=True)
        print(f"Players from {nat}\n")
        for player in self.players:
            if player.nationality == nat:
                lista.append(player)
        return lista
        
