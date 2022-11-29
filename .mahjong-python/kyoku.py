from __future__ import annotations
from random import sample

import mahjong
from mahjong.hand_calculating.hand import HandCalculator
from mahjong.hand_calculating.hand_response import HandResponse
from mahjong.hand_calculating.hand_config import HandConfig
from mahjong.meld import Meld
from mahjong.shanten import Shanten

from constants import Wind
from players.player import Player
from pai import Pai, Paiset, all_pais
from result import MahjongResult


class Kyoku:
    @staticmethod
    def _generate_paishan(
        number_of_players:int,
        has_red:bool
    ) -> Paiset:
        pais:list[Pai] = all_pais(number_of_players, has_red)
        pais = sample(pais, len(pais))
        return Paiset(pais[:-14]), Paiset(pais[-14:])
    
    def __init__(
        self,
        players:list[Player],
        wind:mahjong.constants,
        kyoku_count:int,
        bar_count:int,
        config:HandConfig
    ):
        self.players:list[Player]   = players
        self.wind:mahjong.constants = wind
        self.kyoku_count:int        = kyoku_count
        self.bar_count:int          = bar_count
        self.config:HandConfig      = config
        
        self.hand_calculator:HandCalculator = HandCalculator()
        self.shanten_calculator:Shanten     = Shanten()
        
        self.paishan:Paiset
        self.wangpai:Paiset
        self.paishan, self.wangpai = __class__._generate_paishan(len(self.players), self.config.options.has_aka_dora)
    
    def __next__(self) -> Kyoku:
        assert hasattr(self, 'result')
        if self.result.is_lianzhuang:
            return Kyoku(
                self.players,
                self.wind,
                self.kyoku_count,
                self.bar_count + 1,
                self.config
            )
        elif self.kyoku_count == len(self.players):
            return Kyoku(
                self.players,
                Wind.next_wind(self.wind),
                1,
                0,
                self.config
            )
        else:
            return Kyoku(
                self.players,
                self.wind,
                self.kyoku_count + 1,
                0,
                self.config
            )
            
    def __str__(self):
        return f'{Wind.winds_jp[self.wind]}{self.kyoku_count}局 {self.bar_count}本場'
    
    def _peipai(self):
        peipais = [self.paishan[i * 13:(i + 1) * 13] for i in range(len(self.players))]
        self.paishan = self.paishan[len(self.players) * 13:]
        
        for player, peipai in zip(self.players, peipais):
            player.shoupai = peipai
            player.he = Paiset([])
            
    def _print_paishan(self):
        print(f'牌山: ' + str(self.paishan))
        
    def _print_wangpai(self):
        print(f'王牌: ' + str(self.wangpai))
        
    def _print_shoupai(self, turn:int):
        print(f'{self.players[turn].name}: ' + str(self.players[turn].shoupai.sorted))
        
    def _print_he(self, turn:int):
        print(f'河: ' + str(self.players[turn].he))
        
    def _print_shoupais_n_hes(self):
        for i in range(len(self.players)):
            self._print_shoupai(i)
            self._print_he(i)
        
    def _print_shepai(self, shepai:Pai):
        print(f'捨牌: {shepai}')
            
    def _zimo(self):
        zimo:Paiset = self.paishan[0]
        self.paishan = self.paishan[1:]
        
        return zimo
    
    def _pay(self):
        assert hasattr(self, 'result')
        
        self.result.winner.point += self.result.hand_value.cost['main'] + self.result.hand_value.cost['additional']
        if None == self.result.loser:
            for player in self.players:
                if player is self.result.winner:
                    continue
                if mahjong.constants.EAST == player.wind:
                    player.point -= self.result.hand_value.cost['main']
                else:
                    player.point -= self.result.hand_value.cost['additional']
        else:
            self.result.loser.point -= self.result.hand_value.cost['main']
    
    def run(self, debug:dict[str,bool]) -> MahjongResult:
        self._peipai()
        assert all(hasattr(player, 'shoupai') for player in self.players)
        assert all(hasattr(player, 'he') for player in self.players)
        if debug['wangpai']:
            self._print_wangpai()
        
        turn:int                  = self.kyoku_count - 1
        winner:Player             = None
        loser:Player              = None
        is_liuju:bool             = True
        hand_value:HandResponse   = None
        dora_indicators:Paiset    = Paiset([self.wangpai[0]])
        uradora_indicators:Paiset = Paiset([self.wangpai[5]])
        while len(self.paishan):
            if debug['paishan']:
                self._print_paishan()
            if debug['board']:
                self._print_shoupais_n_hes()
                
            zimo:Paiset = self._zimo()
            self.players[turn].zimo(zimo)
            
            # shanten = self.shanten_calculator.calculate_shanten(self.players[turn].shoupai.to_mahjong34)
            self.config.round_wind  = self.wind
            self.config.player_wind = self.players[turn].wind
            self.config.is_tsumo    = True
            if 0 == len(self.paishan):
                self.config.is_haitei = True
                
            hand_value = self.hand_calculator.estimate_hand_value(
                self.players[turn].shoupai.to_mahjong136,
                zimo.to_mahjong136[0],
                melds=None,
                dora_indicators=dora_indicators.to_mahjong136 + uradora_indicators.to_mahjong136,
                config=self.config
            )
            
            self.config.is_tsumo  = False
            if self.config.is_haitei:
                self.config.is_haitei = False
                self.config.is_houtei = True
                
            if debug['shoupai']:
                self._print_shoupai(turn)
                
            if None != hand_value.han and self.players[turn].hele_chance():
                winner = self.players[turn]
                is_liuju = False
                break
                
            shepai:Pai = self.players[turn].dapai()
            assert 13 == len(self.players[turn].shoupai)
            if debug['shehai']:
                self._print_shepai(shepai)
                
            self.config.is_houtei = False
                
            turn = (turn + 1) % len(self.players)
        
        is_lianzhuang:bool = False if None == winner else (winner.wind == self.wind)
        self.result:MahjongResult = MahjongResult(winner, loser, hand_value, is_liuju, is_lianzhuang)
        
        if winner:
            self._pay()
        
        return self.result
        