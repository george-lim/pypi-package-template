import pytest


def inc(x):
    return x + 1


def test_negative_number():
    assert inc(-1) == 0


def test_zero():
    assert inc(0) == 1


def test_positive_number():
    assert inc(1) == 2


def test_float():
    assert inc(0.000001) == 1.000001


def test_none():
    with pytest.raises(TypeError):
        inc(None)


def test_string():
    with pytest.raises(TypeError):
        inc("1")
