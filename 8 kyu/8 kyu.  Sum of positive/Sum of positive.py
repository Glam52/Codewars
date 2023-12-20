def positive_sum(arr):
    count = 0
    for i in arr:
        if i >= 0:
            count += i
        else:
            count += 0
    return count

# тест
print(positive_sum([1,-2,3,4,5]))
print(positive_sum([-1,2,3,4,-5]))