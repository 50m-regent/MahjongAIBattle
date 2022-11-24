from enum import Enum

import mahjong
from mahjong.constants import EAST, SOUTH, WEST, NORTH, WINDS, HAKU, HATSU, CHUN


class Wind:
    winds_jp:dict[mahjong.constants, str] = {
        EAST:  '東',
        SOUTH: '南',
        WEST:  '西',
        NORTH: '北'
    }
    
    @staticmethod
    def next_wind(wind) -> mahjong.constants:
        return WINDS[(WINDS.index(wind) + 1) % len(WINDS)]


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