punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~0123456789"

def count_words(s):
    s_sans_punct = ""
    for letter in s:
        if letter in punctuation:
            s_sans_punct += " "
        else:
            s_sans_punct += letter
    wds = s_sans_punct.split()
    x = len(wds)
    return x