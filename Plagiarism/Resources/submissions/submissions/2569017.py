def count_words(string):
    inword = False
    count = 0
    for x in string:
        if "a" <= x <= "z" or "A" <= x <= "Z":
            inword = True
        else:
            if inword:
                count += 1
            inword = False
    if inword:
        count += 1
    return count
            