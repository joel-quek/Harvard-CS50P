'''
# fuel.py
# x/y fuel guage
# input x/y, each x and y int's; output % rounded to nearest int
# if < 1% output "E", if > 99% output "F"
# error handling == reprompt
def main():
    while True:
        try:
            percentage = convert(input("Fraction: ").strip())
        except (ValueError, ZeroDivisionError):
            continue
        else:
            if percentage > 100:
                continue
        print(guage(percentage))
        exit(0)

def guage(percentage):
    if percentage <= 1:
        return f"E"
    elif percentage >= 99:
        return f"F"
    else:
        return f"{percentage}%"

# get fraction incl. error handling
def convert(fraction):
    fraction = fraction.split("/")
    f = int(fraction[0]) / int(fraction[1]) * 100
    return round(f)

if __name__ == "__main__":
    main()
'''

'''
from fuel import convert
import pytest

def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("one/two")

if __name__ == "__main__":
    main()
'''

'''
def test_convert():
    with pytest.raises(ValueError):
        convert("shef")
        convert("s/f")
        convert("s/100")
        convert("100/s")
        convert("-1/2")
        convert("2/-1")
        convert("1.5/2")
        convert("7/2")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
        convert("s/0")
#    with pytest.raises(ValueError):
#        for i in [1:10000]:
#            convert(")

def test_gauge():
    assert gauge("1") == "E"
    assert gauge(int("1")) == "E"
    assert gauge("99") == "F"
    assert gauge(int("99")) == "F"

#    with pytest.raises():
