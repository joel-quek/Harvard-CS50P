from jar import Jar
import pytest

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar = Jar(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"

def test_deposit():

def test_withdraw():

def test_errors():
    with pytest raises(ValueError):
        deposit("13")
        withdraw("-2")
