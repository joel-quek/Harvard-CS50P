greeting = input("Greeting: ")

# if greeting starts with "hello" output $0
if greeting.startswith("hello") or greeting.startswith("Hello"):
    print("$0")


# if greeting starts with an "h"" output $20
elif greeting.startswith("h") or greeting.startswith("H"):
    print("$20")

# otherwise output $100
else:
    print("$100")