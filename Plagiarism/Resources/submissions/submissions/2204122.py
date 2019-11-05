def count_words(string):
    inword = False
    count = 0
    for i in string:
        if "a" <= i <= "z" or "A" <= i <= "Z":
            inword = True
        else:
            if inword:
                count += 1
            inword = False
    return count
print(count_words("aa b c8 a"))