import string

def remove_punctuation(s):
    s_without_punctuation = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punctuation += letter
    return s_without_punctuation

def hoofdletters(sentence):
    x = remove_punctuation(sentence)
    y = x.upper()
    return y

def is_palindrome_sentence(sentence2):
    x = hoofdletters(sentence2)
    for i in range(0, int(len(x)/2)):
        if x[i] == x[len(x) -1 -i]:
            return True
        else:
            return False
        break