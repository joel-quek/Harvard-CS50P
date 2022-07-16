def high_and_low(numbers):
    numlist = numbers.split()
    small = numlist[0]
    large = numlist[0]

    for x in numlist:
        if int(x) > int(large):
            large = x

    for x in numlist:
        if int(x) < int(small):
            small = x

    return str(large) + " " + str(small) 