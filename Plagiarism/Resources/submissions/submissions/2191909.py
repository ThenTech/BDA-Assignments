def count_words(s):
    words = 0
    for i in s:
        if i == ' ':
            words += 1
    if s == '':
        return words
    return words + 1