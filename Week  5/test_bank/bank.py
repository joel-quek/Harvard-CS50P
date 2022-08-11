def main():
    shef = input("Greeting: ")
    price = value(shef)
    print(f"${price}")

def value(greeting):
    x = "0"
    if greeting.startswith("hello") or greeting.startswith("Hello") or greeting.startswith(" Hello"):
        x = 0
    elif greeting.startswith("h") or greeting.startswith("H"):
        x = 20
    else:
        x = 100
    return x

if __name__ == "__main__":
    main()