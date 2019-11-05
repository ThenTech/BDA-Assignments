def count_words(string):
    i = 0
    counter = 0
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lastchar = " "
    for ch in string:
        if ch not in alphabet and lastchar in alphabet:
            counter += 1
            lastchar = ch
        elif ch in alphabet:
            lastchar = ch
    if lastchar in alphabet:
        counter += 1
    return counter