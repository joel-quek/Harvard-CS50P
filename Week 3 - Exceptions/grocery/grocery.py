# have an empty dictionary
d = []
l = 0
item=0

# prompt user to input item
while True:
    try:
        # loop input and adding of item
        x = str(input())
        # add item to dictionary
        d.append(x)
        d.sort()
        l = int(len(d))
        # control-D sort and output
    except EOFError:
        counts = {item:d.count(item) for item in d}
        print("")
        for item in counts:
            shef = counts[item]
            print(shef, item.upper())
        break



#        print("")
#        for i in range(l):
#            print (i, d[i])
# What is control-D? EOFError covers Control-D

# I need to: Count repeated entries and output numbers with the fruits
