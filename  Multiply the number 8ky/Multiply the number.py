def multiply(n):            # создана функция по условию
    if n >= 0:
        x = len(str(n))          # узнаем длину числа
    else:
        x = len(str(n)) - 1         # проверка на отрицательное число
    return n * 5 ** x           # умножаем n на 5 в степени x
    pass            # заполнитель по условию

print(multiply(10))
print(multiply(-3))