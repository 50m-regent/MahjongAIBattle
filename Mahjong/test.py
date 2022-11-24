from mahjong_game import Mahjong
from player import Player
from constants import Rule

if __name__ == '__main__':
    game: Mahjong = Mahjong(
        players=[
            Player(),
            Player(),
            Player(),
            Player()
        ],
        rule=Rule.Dongfeng
    )
    game.run()
