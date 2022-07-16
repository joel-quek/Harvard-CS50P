#-------------------------------------------------------------------------------------
import csv
import sys
#-------------------------------------------------------------------------------------
try :
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        file = open(filename)
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif (sys.argv[1].split(".")[1] != "csv"):
        sys.exit("Not a CSV file")

except FileNotFoundError:
    if "." not in sys.argv[1]:
        sys.exit("Not a CSV file")
    elif (sys.argv[1].split(".")[1] != "csv"):
        sys.exit("Not a CSV file")
    elif (sys.argv[1].endswith(".csv") == False):
        sys.exit("Not a CSV file")
    else:
        sys.exit(f"Could not read {sys.argv[1]}")
# -----------------------------------------------------------------------------------
# Changes before.csv into a Python Dictionary or list
reader = csv.reader(file)
data=list(reader) #changes before.csv into a Python list

# Reorganises the Python Dictionary from "Name, House" to "First, Last, House"
after = [] #create new empty list
field_names = ["First", "Last", "House"]
after.append(field_names)

x = int(len(data))


for i in range(1,x):
    full_name = data[i][0]
    last = full_name.split(",")[0]
    first = full_name.split(",")[1]
    house = data[i][1]
    new_input = [first, last, house]
    after.append([first.lstrip(), last, house])

#print (after)

# Changes the Python Dictionary or list into after.csv
file2 = open(sys.argv[2],'w')

with file2:
    writer = csv.writer(file2)

    for row in after:
        writer.writerow(row)