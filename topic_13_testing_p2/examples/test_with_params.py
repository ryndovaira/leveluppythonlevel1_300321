import pytest

params = [
    # x, y, result
    (1, 1, 1),
    (1, 6, 6),
    (1, 6, 7),  # FAIL
    (2, 3, 6)
]

ids = [f"x={x} y={y} res={res}" for (x, y, res) in params]


# scope='function' - выполняется один раз для каждой функции теста
@pytest.fixture(scope="function",
                params=params,
                ids=ids
                )
def param_test(request):
    return request.param


def test_check_mul(param_test):
    (x, y, res) = param_test
    assert x * y == res
