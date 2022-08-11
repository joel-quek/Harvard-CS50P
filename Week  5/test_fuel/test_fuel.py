import fuel
from fuel import convert
from fuel import gauge

import pytest

def test_errors():
    with pytest.raises(ZeroDivisionError):
        convert("100/0")
    with pytest.raises(ValueError):
        convert("s/f")

def test_convert():
    assert convert("1/4") == 25
    assert convert("100/100") == 100
    assert convert("1/3") == 33
    assert convert("0/1") == 0

def test_gauge():
    assert gauge(20) == "20%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
