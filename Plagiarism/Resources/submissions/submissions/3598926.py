def count_words(string):
    i = 0
    x = 0
    while (i < len(string)-2):
        letter = string[i]
        if (not ( "a" <= string[i] <= "z" or "A" <= string[i] <= "Z") and ("a" <= string[i+1] <= "z" or "A" <= string[i+1] <= "Z"))
            x += 1
        i += 1
    return x