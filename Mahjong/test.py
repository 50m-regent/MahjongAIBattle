import mahjong

from mahjong_game import Mahjong
from player import Player
from constants import Rule

if __name__ == '__main__':
    game:Mahjong = Mahjong(
        players=[
            Player(name='a', wind=mahjong.constants.EAST),
            Player(name='b', wind=mahjong.constants.SOUTH),
            Player(name='c', wind=mahjong.constants.WEST),
            Player(name='d', wind=mahjong.constants.NORTH)
        ],
        rule=Rule.Banzhuang,
        terminate_point=0
    )
    game.run(debug=True)
