def is_palindrome_sentence(sentence):
    letters = abcdefghijklmnopqrstuvwxyz
    newline = ''
    for i in sentence:
        if i in letters:
            newline = newline + i
    newline = newline.lower()
    for i in range(newline[len(newline)- 1 + i]):
        newline2 = newline2 + i
    return newline == newline2