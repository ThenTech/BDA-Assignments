def count_words(string):
    inword = False
    count = 0
    for x in string:
        if "a" <= x <= "z" or "A" <= x <= "Z":
            inword = True
        else:
            if inword:
                count = count + 1
            inword = False
    print(count + 1) #laatste woord nog niet uit gegaan
    return count