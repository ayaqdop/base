class Team(object):
    
    MOVES_LEFT = 5
    
    def __init__(self, name, formation, players):
        self.name = name
        self.formation = formation
        self.players = players
        self.score = 0
