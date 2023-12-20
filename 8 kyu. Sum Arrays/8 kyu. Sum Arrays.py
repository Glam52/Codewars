def sum_array(a):
    x = list(map(float, a))     # перевод значений списка в float
    amount = 0       # Lj,fdkty
    for i in x:
        amount += i
    return amount

print(sum_array([1, 5.2, 4, 0, -1]))

