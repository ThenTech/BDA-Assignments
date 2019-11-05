punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~0123456789"

def remove_punctuation(s):
    s_sans_punct = ""
    for letter in s:
        if letter in punctuation:
            s_sans_punct += " "
        else:
            s_sans_punct += letter
    return s_sans_punct

def count_words(string):
    wds = string.split()
    x = len(wds)
    return x
    
count_words(remove_punctuation(ss))