class Player:

    MOVES_LEFT = 3

    def __init__(self, team, number):
        self.team = team
        self.number = number
        self.moves_left = Player.MOVES_LEFT

    def __str__(self):
        return str(self.number)
