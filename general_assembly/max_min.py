def minimum(arr):
    x = arr[0]
    for y in arr:
        if int(y) < int(x):
            x = y
    return x

def maximum(arr):
    x = arr[0]
    for y in arr:
        if int(y) > int(x):
            x = y
    return x
    