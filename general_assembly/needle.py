def find_needle(haystack):
    x = list(enumerate(haystack))
    for y in x:
       if y[1] == 'needle':
        return "found the needle at position" + " " + str(y[0])
             