def count_words(s):
    words = 0
    for i in s:
        if i == ' ':
            words += 1
    if s[len(s)-1] != None:
        words += 1
    return words