import string


def count_words(s):
    for i in range(len(s)):
        if s[i] in string.punctuation:
            s = s.replace(s[i], " ")
    arr = s.split()
    count = 0
    for i in arr:
        isstring = True
        for j in i:
            if not ("A" <= i <= "Z" or "a" <= i <= "z"):
                isstring = False
        if isstring:
            count += 1
    return count