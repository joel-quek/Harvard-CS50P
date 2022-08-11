import inflect

d = []
# mylist = 0
# name = 0
p = inflect.engine() #what is this for?


name = input("Name: ")
# adieu_output = "Adieu, adieu, to "

try:
    while len(name) > 0:
        d.append(name)
        mylist = p.join(d)
        name = input("Name: ")
except EOFError: #this is the ctrl+D portion
    print("\nAdieu, adieu, to", mylist)







    # while True:
#     name = input("Name: ")
#     d.append(name)
#     mylist = p.join(d)

#    print("Adieu, adieu, to ", mylist)