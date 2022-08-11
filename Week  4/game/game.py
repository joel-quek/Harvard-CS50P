import random

while True:
    try:
        n = int(input("Level: "))
        x = random.randint(1,n)
        break
    except ValueError:
        pass
# Correct up till line 9. Now need to prompt the guess and check.

randomint = x

while True:
    try:
        y = int(input("Guess: "))
        if y == randomint:
            print("Just right!")
            break
        elif y < randomint:
            print ("Too small!")
        elif y > randomint:
            print("Too large!")
    except y < randomint:
        pass
    except y > randomint:
        pass
# code runs and passes when y is smaller or larger. But does not print "Too small" or "Too large"