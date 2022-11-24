from __future__ import annotations

import mahjong

from constants import Wind
from player import Player
from result import MahjongResult

class Kyoku:
    def __init__(
        self,
        players:list[Player],
        wind:mahjong.constants,
        kyoku_count:int,
        bar_count:int
    ):
        self.players:list[Player]   = players
        self.wind:mahjong.constants = wind
        self.kyoku_count:int        = kyoku_count
        self.bar_count:int          = bar_count
    
    def __next__(self) -> Kyoku:
        assert hasattr(self, 'result')
        if self.result.is_lianzhuang:
            return Kyoku(
                self.players,
                self.wind,
                self.kyoku_count,
                self.bar_count + 1
            )
        elif self.kyoku_count == len(self.players):
            return Kyoku(
                self.players,
                Wind.next_wind(self.wind),
                1,
                0
            )
        else:
            return Kyoku(
                self.players,
                self.wind,
                self.kyoku_count + 1,
                0
            )
            
    def __str__(self):
        return f'{Wind.winds_jp[self.wind]}{self.kyoku_count}局 {self.bar_count}本場'
    
    def run(self) -> MahjongResult:
        self.result:MahjongResult = MahjongResult(winner=self.players[0])
        
        return self.result
        