import mahjong

from constants import Rule
from players.player import Player
from kyoku import Kyoku
from result import MahjongResult


class Mahjong:
    def __init__(
        self,
        players:list[Player],
        rule:Rule,
        terminate_point:int=30000
    ):
        assert len(players) in [3, 4]
        self.players:list[Player] = players
        self.rule:Rule            = rule
        self.terminate_point:int  = terminate_point
        
        self.kyoku:Kyoku = Kyoku(
            players=self.players,
            wind=mahjong.constants.EAST,
            kyoku_count=1,
            bar_count=0,
        )

    def _is_game_end(self) -> bool:
        if all(player.point < self.terminate_point for player in self.players):
            return False
        
        if Rule.Dongfeng == self.rule:
            return mahjong.constants.EAST != self.kyoku.wind
        elif Rule.Banzhuang == self.rule:
            return self.kyoku.wind not in [mahjong.constants.EAST, mahjong.constants.SOUTH]
        
        return True

    def run(self, debug:bool=False):
        while not self._is_game_end():
            if debug:
                print()
                print(self.kyoku)
                [*map(print, self.players)]
                
            result:MahjongResult = self.kyoku.run(debug)
            
            if debug:
                print(result)
            
            if not result.is_lianzhuang:
                [*map(lambda player:player.iterate_wind(), self.players)]
            
            self.players.sort(key=lambda player:player.wind)
            self.kyoku = next(self.kyoku)
            