def even_or_odd(number):            # функция по условию
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
    pass            # заполнитель по условию

n = int(input())
print(even_or_odd(n))