from overrides import override

from players.player import Player
from pai import Pai


class GreedyPlayer(Player):
    @override
    def hele_chance(self) -> bool:
        return True
    
    @override
    def dapai(self) -> Pai:
        assert hasattr(self, 'shoupai')
        
        self.shoupai = self.shoupai.sorted
        shepai:Pai = self.shoupai.pop(-1)
        self.he.append(shepai)
        
        return shepai
