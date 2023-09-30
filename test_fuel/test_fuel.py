from fuel import convert, gauge
import pytest

def test_fraction():
    assert convert("3/4") == 75
    assert convert("0/4") == 0

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"

def test_zerodiv():
    with pytest.raises(ZeroDivisionError):
       assert convert("4/0")

def test_valerror():
    with pytest.raises(ValueError):
        assert convert("5/4")
        assert convert("-1/3")