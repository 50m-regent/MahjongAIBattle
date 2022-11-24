from __future__ import annotations
from random import sample

import mahjong
from mahjong.hand_calculating.hand import HandCalculator
from mahjong.tile import TilesConverter
from mahjong.hand_calculating.hand_config import HandConfig, OptionalRules
from mahjong.meld import Meld

from constants import Wind
from players.player import Player
from pai import Pai, Paiset, all_pais
from result import MahjongResult


class Kyoku:
    @staticmethod
    def _generate_paishan(number_of_players:int) -> Paiset:
        pais:list[Pai] = all_pais(number_of_players)
        pais = sample(pais, len(pais))
        return Paiset(pais[:-14]), Paiset(pais[-14:])
    
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
        
        self.calculator:HandCalculator = HandCalculator()
        
        self.paishan:Paiset
        self.wangpai:Paiset
        self.paishan, self.wangpai = __class__._generate_paishan(len(self.players))
    
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
    
    def _peipai(self):
        peipais = [self.paishan[i * 13:(i + 1) * 13] for i in range(len(self.players))]
        self.paishan = self.paishan[len(self.players) * 13:]
        
        for player, peipai in zip(self.players, peipais):
            player.shoupai = peipai
            
    def _print_paishan(self):
        # print(f'牌山(余{len(self.paishan)}): ' + str(self.paishan))
        print(f'牌山: ' + str(self.paishan))
        
    def _print_wangpai(self):
        print(f'王牌: ' + str(self.wangpai))
        
    def _print_shoupai(self, turn:int):
        print(f'{self.players[turn].name}: ' + str(self.players[turn].shoupai.sorted))
        
    def _print_shepai(self, shepai:Pai):
        print(f'捨牌: {shepai}')
            
    def _zimo(self, turn:int):
        self.players[turn].shoupai += self.paishan[0]
        self.paishan = self.paishan[1:]
    
    def run(self, debug:bool) -> MahjongResult:
        self._peipai()
        assert all(hasattr(player, 'shoupai') for player in self.players)
        if debug:
            self._print_wangpai()
        
        turn:int = self.kyoku_count - 1
        while len(self.paishan):
            if debug:
                self._print_paishan()
                
            self._zimo(turn)
            if debug:
                self._print_shoupai(turn)
                
            shepai:Pai = self.players[turn].dapai()
            assert 13 == len(self.players[turn].shoupai)
            if debug:
                self._print_shepai(shepai)
            
            turn = (turn + 1) % len(self.players)
        
        self.result:MahjongResult = MahjongResult(winner=None)
        
        return self.result
        