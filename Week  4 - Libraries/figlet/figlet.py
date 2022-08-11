import pyfiglet
import sys

from pyfiglet import Figlet



if len(sys.argv)>2 and sys.argv[1] in ["-f","-font"] and sys.argv[2] in ["rectangles", "slant", "alphabet"]:
    x = input("Input: ")
    result = pyfiglet.figlet_format(x, font = sys.argv[2])
    print("Output:", result)

else:
    sys.exit("Invalid Usage")

#if len(sys.argv)<2 or sys.argv[1] != "-f" or sys.argv[1] != "--font" or sys.argv[2] != "slant" or sys.argv[2] != "rectangles" or sys.argv[2] != "alphabet":