import pytest
import sieve
from sieve import get_input, create_integer_list, the_sieve, remove_composite_list
'''
def test_get_input():
    with pytest.raises(ValueError):
        get_input("-2")
        get_input("0")
    assert get_input("3") == int(3)
    assert get_input("12") == int(12)
'''
def test_create_integer_list():
    assert create_integer_list (12) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert create_integer_list (14) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

def test_the_sieve():
    assert the_sieve([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 12)==[2, 4, 6, 8, 10, 12]
    assert the_sieve([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14], 14)==[2, 4, 6, 8, 10, 12, 14]

def test_remove_composite_list():
    list1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14]
    list2 = [2, 4, 6, 8, 10, 12, 14]
    assert remove_composite_list(list1, list2) == [3, 7, 9, 11, 13]