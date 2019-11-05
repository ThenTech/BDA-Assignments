def is_palindrome_sentence(sentence):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    newline = ''
    newline2 = ''
    for i in sentence:
        if i in letters:
            newline += i
    newline = newline.lower()
    for j in range(len(newline)):
        newline2 += newline[len(newline)- 1 - j]
    return newline == newline2