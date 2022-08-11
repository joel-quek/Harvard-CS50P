import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    matches = re.search(r"(http(s)*)(\:\/\/)(www\.)*(youtube\.com)(\/embed\/)([a-zA-Z0-9]+)", s)
    if matches:
        a, b, c, d, e, f, g = matches.groups()
        return f"https://youtu.be/{g}"
    else:
        return "None"

if __name__=="__main__":
    main()