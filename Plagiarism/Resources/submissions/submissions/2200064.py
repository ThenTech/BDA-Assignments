def count_words(string):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counter = 0
    lastchar = "."
    for i in string:
        if i not in alphabet and lastchar in alphabet:
            counter += 1
            lastchar = i
        elif i not in alphabet:
            lastchar = i
    if lastchar in alphabet:
        counter += 1
    return counter
