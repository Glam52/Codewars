def disemvowel(string_):
    string_ = list(string_)
    for i in string_[::-1]:
        if i in 'eioa':
            string_.remove(i)

    return str(''.join(string_))

print(disemvowel('This website is for losers LOL!'))