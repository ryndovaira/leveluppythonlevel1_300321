from topic_02_syntax.practice.logic_3_check_numbers_by_5 import check_numbers_by_5


def test_logic_3_check_numbers_by_5_ep_ok():
    assert check_numbers_by_5(1, 2, 6) == True
    assert check_numbers_by_5(1, 6, 2) == True
    assert check_numbers_by_5(6, 1, 2) == True

    assert check_numbers_by_5(1, 1, 2) == False


# def test_logic_3_check_numbers_by_5_ep_wrong():
#     assert check_numbers_by_5("3", "2", "6")
