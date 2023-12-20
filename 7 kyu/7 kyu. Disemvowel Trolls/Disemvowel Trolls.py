def disemvowel(string_):
    string_ = list(string_)
    for i in string_[::-1]:
        if i in 'eioauEIOAU':
            string_.remove(i)

    return str(''.join(string_))

print(disemvowel('This website is for losers LOL!'))