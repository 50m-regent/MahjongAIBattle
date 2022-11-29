import mahjong
from mahjong.hand_calculating.hand_config import HandConfig, OptionalRules, HandConstants

from mahjong_game import Mahjong
from players.greedy import GreedyPlayer
from constants import Rule


if __name__ == '__main__':
    game:Mahjong = Mahjong(
        players=[
            GreedyPlayer(name='a', wind=mahjong.constants.EAST),
            GreedyPlayer(name='b', wind=mahjong.constants.SOUTH),
            GreedyPlayer(name='c', wind=mahjong.constants.WEST),
            GreedyPlayer(name='d', wind=mahjong.constants.NORTH)
        ],
        rule=Rule.Dongfeng,
        config=HandConfig(
            is_tsumo=False,
            is_riichi=False,
            is_ippatsu=False,
            is_rinshan=False,
            is_chankan=False,
            is_haitei=False,
            is_houtei=False,
            is_daburu_riichi=False,
            is_nagashi_mangan=False,
            is_tenhou=False,
            is_renhou=False,
            is_chiihou=False,
            paarenchan=0,
            options=OptionalRules(
                has_open_tanyao=True,
                has_aka_dora=True,
                has_double_yakuman=True,
                kazoe_limit=HandConstants.KAZOE_NO_LIMIT,
                kiriage=False,
                fu_for_open_pinfu=True,
                fu_for_pinfu_tsumo=True,
                renhou_as_yakuman=True,
                has_daisharin=True,
                has_daisharin_other_suits=True,
                limit_to_sextuple_yakuman=False,
                paarenchan_needs_yaku=False,
                has_daichisei=True,
            )
        ),
        terminate_point=0
    )
    game.run(debug={
        'kyoku': True,
        'wangpai': True,
        'paishan': False,
        'board': False,
        'shoupai': False,
        'shehai': False
    })
