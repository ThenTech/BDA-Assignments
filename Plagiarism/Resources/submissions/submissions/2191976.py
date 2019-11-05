import string

def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct


def count_words(s):
    s = remove_punctuation(s)
    return len(s.split())