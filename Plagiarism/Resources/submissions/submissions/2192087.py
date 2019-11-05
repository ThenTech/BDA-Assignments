import string

def remove_punc(string):
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    string_punc = ""
    for letter in string:
        if letter not in punctuation:
            string_punc += letter

def count_words(string):
    z = remove_punc(string)
    x = len(str(z).split())
    return x