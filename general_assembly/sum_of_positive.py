def positive_sum(arr):
    sum = 0
    for num in arr:
        if int(num) > 0:
            sum = sum + num
    return sum