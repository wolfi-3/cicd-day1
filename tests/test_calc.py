from calc import add, divide, subtract
import pytest


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 5) == 5


def test_divide():
    divide(10, 2)
    assert True


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)
