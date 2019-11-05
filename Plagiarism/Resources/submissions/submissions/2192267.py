import string

def remove_punctuation(s):
    s_without_punct = ''
    for letter in s:
        if letter in string.punctuation:
            s_without_punct += ' '
        if letter not in string.punctuation:
            s_without_punct += letter
        
    return s_without_punct

def count_words(string):
    string = remove_punctuation(string)
    s_without_int = ''
    for i in string:
        if i not in '123456789':
            s_without_int += i
    x = s_without_int.split()
    x = len(x)
    return x