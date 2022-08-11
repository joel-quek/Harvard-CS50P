import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if ".py" not in sys.argv[1]:
    sys.exit("Not a Python File")

try :
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        file = open(filename)
#        print(len(file.readlines()))


except FileNotFoundError:
        sys.exit("File does not exist")

lines = file.readlines()
count = 0
#print(lines)
for line in lines:
    if line.startswith('\n') or line.startswith('#') or line.isspace() or line.lstrip().startswith('#'):
        count = count + 1

#print(lines)
print(len(lines) - count)

#submitted on 3 June 2022, Friday