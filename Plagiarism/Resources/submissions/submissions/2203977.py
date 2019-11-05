def count_words(string):
    inword = False
    Teller = 0
    for x in string:
        if "a" <= x <= "z" or "A" <= x <= "Z":
            inword = True
        else:
            if inword:
                Teller += 1
                inword = False
    if inword == True:
        Teller += 1
    return Teller