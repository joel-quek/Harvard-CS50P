list = ['s', 'h', 'e', 'f', '0', '2', '3', '4']

sublistalpha = [x for x in list if x.isalpha()]

sublistnum = [x for x in list if x.isdigit()]

print(sublistalpha)

print (sublistnum)

if sublistnum[1] == 0:
    print ("False")

indexfirst = 2
shef = list.index(indexfirst)
print(shef)