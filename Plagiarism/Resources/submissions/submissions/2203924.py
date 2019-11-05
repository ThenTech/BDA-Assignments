def count_words(string):
    inword = False
    teller = 0
    
    for letter in string:
        if "a" <= letter <= "z" or "A" <= letter <= "Z":
            inword = True
        else:
            if inword:
                teller = teller + 1
            inword = False
    if inword:
        teller = teller + 1
    return teller