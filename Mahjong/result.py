from players.player import Player


class MahjongResult:
    def __init__(
        self,
        winner:Player
    ):
        self.winner = winner
        
        self.is_lianzhuang = False
        
    def __str__(self):
        return_string = ''
        if None == self.winner:
            return_string += '流局'
        else:
            return_string += f'和: {self.winner.name}'
        
        return return_string