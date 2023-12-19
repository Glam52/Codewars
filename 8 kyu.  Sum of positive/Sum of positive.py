def positive_sum(arr):
    count = 0
    for i in arr:
        if i >= 0:
            count += i
        else:
            count += 0
    return 0