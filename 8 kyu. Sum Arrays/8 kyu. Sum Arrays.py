def sum_array(a):
    x = list(map(float, a))
    count = 0
    for i in x:
        count += i
    return count

print(sum_array([1, 5.2, 4, 0, -1]))

