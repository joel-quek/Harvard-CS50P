from bank import value
#from bank import bank

def test_value ():
    assert value ("Hello") == 0
    assert value ("Hello, Newman") == 0
    assert value ("How you doing?") == 20
    assert value ("What's happening?") == 100
    assert value ("hello newman") == 0
    assert value ("hello") != ValueError
    assert value ("hello") != 20
    assert value ("hello") != 100
# submitted