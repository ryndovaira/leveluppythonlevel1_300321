from topic_2_syntax.practice.logic_0_season import *


def test_seasons_ok():
    assert season(12) == season(1) == season(2) == "Winter"
    assert season(3) == season(4) == season(5) == "Spring"
    assert season(6) == season(7) == season(8) == "Summer"
    assert season(9) == season(10) == season(11) == "Fall"


def test_seasons_wrong():
    assert season(0) is None
    assert season(13) is None
    assert season(66) is None
