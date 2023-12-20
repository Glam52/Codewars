def grow(arr):
    import math     # импорт модуля для умножения списка
    num = list(map(int, arr))       # перевол списка в int
    return math.prod(num)

#тест
print(grow([1, 2, 3, 4]))

