import mahjong
from mahjong.hand_calculating.hand import HandCalculator
from mahjong.tile import TilesConverter
from mahjong.hand_calculating.hand_config import HandConfig, OptionalRules
from mahjong.meld import Meld

from player import Player
from rule import Rule
from kyoku import Kyoku

class Mahjong:
    def __init__(
        self,
        players: list[Player],
        rule: Rule
    ):
        self.calculator: HandCalculator = HandCalculator()

        assert len(players) in [3, 4]
        self.players: list[Player] = players
        self.rule: Rule = rule

        self.field_wind: mahjong.constants = mahjong.constants.EAST
        self.kyoku_count: int = 1

    def run(self):
        pass