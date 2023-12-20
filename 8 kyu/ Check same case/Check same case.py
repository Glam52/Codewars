def same_case(a, b):
    if not a.isalpha() or not b.isalpha():
        return  -1          # если не буквы вернуть -1
    elif a.islower() and b.islower():
        return 1            # проверка нижнего регистра
    elif a.isupper() and b.isupper():
        return 1            # проверка верхнего регистра
    else:
        return 0            # остальное
    pass # новый комментарий