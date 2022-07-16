camel = input("camelCase: ")

for c in camel:
    if c.isupper():
        camel = camel.replace (c, "_" + c.lower())
#     break


camel = camel.lower()

print("snake_case:", camel)