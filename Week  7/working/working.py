import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
    # input 9:00 AM to 5:00 PM
    firstcase = re.search(r"([1-9]|[0-1][0-2])\:([0-5][0-9]) (AM|PM) to ([1-9]|[0-1][0-2])\:([0-5][0-9]) (AM|PM)",s)

    # # or 9 AM to 5 PM
    secondcase = re.search(r"([1-9]|[0-1][0-2]) (AM|PM) to ([1-9]|[0-1][0-2]) (AM|PM)", s)

    if firstcase:
        a, b, c, d, e, f = firstcase.groups()

        if a == "12" and c == "AM":
            a = "00"
        elif d == "12" and f == "AM":
            d = "00"

        if c == "PM" and a != "12":
            a = int(a) + 12
        elif f == "PM" and d != "12":
            d = int(d) + 12

        output = str(f"{a}:{b} to {d}:{e}")

        return (output)

    elif secondcase:
        a, b, c, d = secondcase.groups()
        if b == "PM" and a != "12":
            a = int(a) + 12
        if d == "PM" and c != "12":
            c = int(c) + 12
        if a == "12" and b == "AM":
            a = "00"
        if c == "12" and d == "AM":
            c = "00"
        output = str(f"{a}:00 to {c}:00")

        return (output)

    else:
        raise ValueError


if __name__ == "__main__":
    main()