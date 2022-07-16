#-------------------------------------------------------------------------------------
import csv # SUBMITTED ON 3 JUNE 2022 FRIDAY
import sys
from tabulate import tabulate
# ------------------------------------------------------------------------------------
try :
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        file = open(filename)
#        print(len(file.readlines()))
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
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
        sys.exit("File does not exist")
# -----------------------------------------------------------------------------------

reader = csv.reader(file)
data=list(reader)

print(tabulate(data, tablefmt="grid", headers = "firstrow"))

#source: https://stackoverflow.com/questions/24662571/python-import-csv-to-list
#------------------------------------------------------------------------------------
# lines = file.readlines()
#pizzatable = []

#for line in file:
#    ptype, smallprice, largeprice = line.rstrip().split(",")
#    pizzarow = {"pizzatype": ptype, "smallprice": smallprice, "largeprice": largeprice}
#    pizzatable.append(pizzarow)

#print(pizzatable)
#print(tabulate(lines))
#----------------------------------------------------------------------------------------