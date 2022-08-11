d= {"Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00}
price = 0
pricestr = 0

while True:
    try:
        item = input("Item: ")
        item = item.title()
        if item in d:
            price = d[item] + price
            pricestr = "{:.2f}".format(price)
            pricestr = pricestr.lstrip()
            print(f"Total: ${pricestr}")

    except KeyError:
        pass

    except EOFError:
        print("\n")
        break