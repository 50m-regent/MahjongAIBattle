from enum import Enum

import mahjong

class Wind:
    winds:list[mahjong.constants] = [
        mahjong.constants.EAST,
        mahjong.constants.SOUTH,
        mahjong.constants.WEST,
        mahjong.constants.NORTH
    ]
    winds_jp:dict[mahjong.constants, str] = {
        mahjong.constants.EAST:  '東',
        mahjong.constants.SOUTH: '南',
        mahjong.constants.WEST:  '西',
        mahjong.constants.NORTH: '北'
    }
    
    @classmethod
    def next_wind(cls, wind) -> mahjong.constants:
        return cls.winds[(cls.winds.index(wind) + 1) % len(cls.winds)]

class Rule(Enum):
    Dongfeng  = 0
    Banzhuang = 1