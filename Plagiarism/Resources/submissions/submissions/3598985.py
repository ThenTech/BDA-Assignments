def count_words(string):
    inword = True
    totwords = 0
    i = 0
    while i < len(string)-1:
        if "a" <= string[i] <= "z" or "A" <= string[i] <= "Z":
            inword = True
        elif not inword:
            i += 1
            continue
        else:
            inword = False
            totwords += 1
        i += 1
    if inword:
     totwords += 1
    return totwords