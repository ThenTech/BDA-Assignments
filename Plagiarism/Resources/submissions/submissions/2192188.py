punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~0123456789 "

def is_palindrome_sentence(sentence):
    ss = ""
    for letter in sentence:
        if letter not in punctuation:
            ss += letter

    i = 0
    j = len(ss) - 1
    while i <= len(ss) / 2:
        if ss[i] == ss[j]:
            i += 1
            j -= 1
        else:
            return  False
    return  True
     