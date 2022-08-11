d = {"apple": "130","avocado":"50", "banana":"110", "sweet cherries": "100" , "cantaloupe": "50", "grapefruit": "60", "kiwifruit" : "90", "pear":"100"}

shef = input("Item: ").lower()
#ind = int(d.index[shef])

if shef in d:
    print("Calories:", d[shef])
else:
    None
#print(d[ind])