import pytest

from topic_13_testing_p2.examples.errors import divide, my_error


def test_divide():
    with pytest.raises(ZeroDivisionError) as exc_info:
        divide(10, 0)

    assert 'my zero' in str(exc_info.value)


def test_my_error():
    with pytest.raises(Exception) as exc_info:
        my_error()

    assert 'my error' in str(exc_info.value)
