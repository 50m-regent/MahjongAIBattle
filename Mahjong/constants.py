from enum import Enum

import mahjong
from mahjong.constants import EAST, SOUTH, WEST, NORTH, HAKU, HATSU, CHUN


class Wind:
    winds:list[mahjong.constants] = [
        EAST,
        SOUTH,
        WEST,
        NORTH
    ]
    winds_jp:dict[mahjong.constants, str] = {
        EAST:  '東',
        SOUTH: '南',
        WEST:  '西',
        NORTH: '北'
    }
    
    @classmethod
    def next_wind(cls, wind) -> mahjong.constants:
        return cls.winds[(cls.winds.index(wind) + 1) % len(cls.winds)]


class Dragon:
    dragons:list[mahjong.constants] = [
        HAKU,
        HATSU,
        CHUN
    ]
    dragons_jp:dict[mahjong.constants, str] = {
        HAKU:  '白',
        HATSU: '發',
        CHUN:  '中'
    }


class Rule(Enum):
    Dongfeng  = 0
    Banzhuang = 1