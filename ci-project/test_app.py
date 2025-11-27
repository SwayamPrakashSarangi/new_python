import app


def test_add_positive():
    assert app.add(2, 3) == 5


def test_add_negative():
    assert app.add(-1, -1) == -2


def test_subtract():
    assert app.subtract(5, 3) == 2
    assert app.subtract(0, 4) == -4
    assert app.subtract(-2, -3) == 1
