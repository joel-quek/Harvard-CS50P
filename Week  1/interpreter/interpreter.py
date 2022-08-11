shef = input("Expression: ")

x, y, z = shef.split(" ")

x2 = float(x)
operation = y
z2 = float(z)

if operation == "+":
    sum = x2 + z2
    print (sum)

elif operation == "-":
    difference = x2 - z2
    print(difference)

elif operation == "*":
    product = x2 * z2
    print(product)

elif operation == "/":
    quotient = x2/z2
    print (quotient)