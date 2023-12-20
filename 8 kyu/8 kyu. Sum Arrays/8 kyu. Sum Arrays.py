def sum_array(a):
    x = list(map(float, a))  # перевод значений списка в float
    amount = 0  # сумма списка
    for i in x:  # цикл перебирающий значения списка
        amount += i  # суммирование значений списка
    return amount

# тест
print(sum_array([1, 5.2, 4, 0, -1]))
print(sum_array([1, 2, 3]))
print(sum_array([1.1, 2.2, 3.3]))
print(sum_array([4, 5, 6]))
print(sum_array(range(101)))
