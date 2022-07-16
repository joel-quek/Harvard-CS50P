def pairs(arr):
    if is_even(len(arr)) == True:
        x = list(range(len(arr))) # produces list of indices
        skip = x[0: len(x): 2]
        cons_count = 0
        for first in skip:
            if (arr[int(first)] - arr[int(first)+int(1)] == 1) or (arr[int(first)+int(1)] - arr[int(first)]== 1):
                    cons_count = cons_count + 1
            else:
                pass
        return cons_count

    elif is_even(len(arr)) == False:
        arr.pop(-1)
        x = list(range(len(arr))) # produces list of indices
        skip = x[0: len(x): 2]
        cons_count = 0
        for first in skip:
            if (arr[int(first)] - arr[int(first)+int(1)] == 1) or (arr[int(first)+int(1)] - arr[int(first)]== 1):
                    cons_count = cons_count + 1
            else:
                pass
        return cons_count

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False