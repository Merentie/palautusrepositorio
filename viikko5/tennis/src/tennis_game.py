class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        elif player_name == "player2":
            self.player2_score += 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.score_is_tied()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.player_has_an_advantage_or_has_won()
        else:
            return self.other_scoring_scenarios()

    def score_is_tied(self):
        if self.player1_score == 0:
            return "Love-All"
        elif self.player1_score == 1:
            return "Fifteen-All"
        elif self.player1_score == 2:
            return "Thirty-All"
        else:
            return "Deuce"
    
    def player_has_an_advantage_or_has_won(self):
        point_difference = self.player1_score - self.player2_score
        if point_difference == 1:
            return "Advantage player1"
        elif point_difference == -1:
            return "Advantage player2"
        elif point_difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def other_scoring_scenarios(self):
        scoring_dictionary = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        return scoring_dictionary[self.player1_score] + "-" + scoring_dictionary[self.player2_score]