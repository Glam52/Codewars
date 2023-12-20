def disemvowel(string_):
    string_ = list(string_)     # перевод строки в список
    for i in string_[::-1]:     # перебор списка посимвольно с конца
        if i in 'eioauEIOAU':       # проверка на гласные
            string_.remove(i)       # удаление гласных

    return str(''.join(string_))        # возврат строки

# тест
print(disemvowel('This website is for losers LOL!'))