from abc import abstractmethod

import mahjong

from constants import Wind
from pai import Pai, Paiset


class Player:
    def __init__(
        self,
        name:str,
        wind:mahjong.constants,
        point:int=25000
    ):
        self.name:str               = name
        self.wind:mahjong.constants = wind
        self.point:int              = point
        
        self.he = Paiset([])
        
    def __str__(self):
        return f'{Wind.winds_jp[self.wind]} {self.name} {self.point:>6}'
    
    def iterate_wind(self):
        self.wind = Wind.next_wind(self.wind)
        
    @abstractmethod
    def dapai(self) -> Pai:
        pass
        