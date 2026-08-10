from calc import add, divide, subtract
import pytest
import random
import time


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 5) == 5


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_flaky_timing():
    start = time.time()
    time.sleep(0.01)
    elapsed = time.time() - start
    assert elapsed < 0.015
    assert random.random() > 0.5
