class Player(object):

    MOVES_LEFT = 3

    def __init__(self, team, number):
        self.team = team
        self.number = number
        self.moves_left = Player.MOVES_LEFT
