from random import randrange

from overrides import override

from players.player import Player
from pai import Pai


class RandomPlayer(Player):
    @override
    def dapai(self) -> Pai:
        shepai:Pai = self.shoupai.pop(randrange(0, len(self.shoupai)))
        self.he.append(shepai)
        
        return shepai
