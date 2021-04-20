from topic_02_syntax.practice.logic_3_check_numbers_by_5 import check_numbers_by_5


def test_logic_3_check_numbers_by_5_ep_ok():
    assert check_numbers_by_5(1, 2, 6)  # не == и не is True, так как это излишне
    assert check_numbers_by_5(1, 6, 2)  # не == и не is True, так как это излишне
    assert check_numbers_by_5(6, 1, 2) is True  # не ==

    assert check_numbers_by_5(1, 1, 2) is False  # не ==

# def test_logic_3_check_numbers_by_5_ep_wrong():
#     assert check_numbers_by_5("3", "2", "6")
