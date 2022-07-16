months =["January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]
# input: month-day-year (eg: 9/8/1636 or September 8, 1636)
# output: YYYY-MM-DD
while True:
    try:
        d = input("Date: ")
        x,y,z = d.split("/")
        x = int(x)
        y = int(y)
        z = int(z)
        if x <=12 and y <=31:
            print(f"{z}-{x:02}-{y:02}")
            break
#        else:
#            pass


    except ValueError:
        x,y,z = d.split(" ")
        y=y.replace(","," ")
        y = int(y)
        z = int(z)
        if y <= 31:
            x = (months.index(x))+1
            x=int(x)
            print(f"{z}-{x:02}-{y:02}")
            break
    else:
        pass





