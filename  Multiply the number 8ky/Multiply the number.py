def multiply(n):            # создана функция по условию
    x = len(str(n))          # узнаем длину числа
    return n * 5 ** x           # умножаем n на 5 в степени x
    pass            # заполнитель по условию

print(multiply(10))