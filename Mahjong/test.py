import mahjong

from mahjong_game import Mahjong
from players.random import RandomPlayer
from constants import Rule


if __name__ == '__main__':
    game:Mahjong = Mahjong(
        players=[
            RandomPlayer(name='a', wind=mahjong.constants.EAST),
            RandomPlayer(name='b', wind=mahjong.constants.SOUTH),
            RandomPlayer(name='c', wind=mahjong.constants.WEST),
            RandomPlayer(name='d', wind=mahjong.constants.NORTH)
        ],
        rule=Rule.Banzhuang,
        terminate_point=0
    )
    game.run(debug=True)
