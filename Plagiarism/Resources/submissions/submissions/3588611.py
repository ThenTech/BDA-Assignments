def count_words(s):
    length_s = len(s)
    counter = 0

    for i in range(0, length_s):
        if (s[i] in string.punctuation or s[i] == " "):
            counter += 1
        elif(i == (len(s) - 1) and s[i] not in string.punctuation):
            counter += 1
    return counter