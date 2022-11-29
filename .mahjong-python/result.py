from mahjong.hand_calculating.hand_response import HandResponse

from players.player import Player


class MahjongResult:
    def __init__(
        self,
        winner:Player,
        loser:Player,
        hand_value:HandResponse,
        is_liuju:bool,
        is_lianzhuang:bool
    ):
        self.winner:Player = winner
        self.loser:Player = loser
        self.hand_value:HandResponse = hand_value
        self.is_lianzhuang:bool = is_lianzhuang
        
    def __str__(self):
        return_string = ''
        if None == self.winner:
            return_string += '流局'
        else:
            return_string += f'和: {self.winner.name} {self.winner.shoupai}\n'
            return_string += f'{self.hand_value.yaku}\n'
            return_string += f'{self.hand_value.han}飜 {self.hand_value.fu}符\n'
            return_string += f'{self.hand_value.cost}'
        
        return return_string