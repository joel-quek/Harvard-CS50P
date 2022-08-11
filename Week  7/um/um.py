import re
import sys

def main():
    print(count(input("Text: ")))


def count(s):
    shef = re.findall(r"\W*um\W*", s, re.IGNORECASE)
    return len(shef)


if __name__ == "__main__":
    main()