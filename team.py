class Team:

    MOVES_LEFT = 5

    def __init__(self, name, formation, players):
        self.name = name
        self.formation = formation
        self.players = players
        self.score = 0
        self.moves_left = Team.MOVES_LEFT
