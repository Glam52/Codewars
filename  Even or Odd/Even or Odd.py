def even_or_odd(number):            # функция по условию
    if number % 2 == 0:         # остаток при делении на 2
        return 'Even'
    else:
        return 'Odd'
    pass            # заполнитель по условию

#проверка, в заданиен не входит
n = int(input())
print(even_or_odd(n))