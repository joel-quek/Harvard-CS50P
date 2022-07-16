import um
from um import count
import pytest


def test_cs50p_given_test_inputs():
    assert count('Um, thanks for the album.') == 1
    assert count('Um, thanks, um...') == 2

def test_between_spaces_and_punctuation():
    assert count('um?!')== 1
    assert count ('Hi, um how are you?') == 1

def test_um_inside_word():
    assert count('clumsy') == 0

if __name__ == "__main__":
    main()

