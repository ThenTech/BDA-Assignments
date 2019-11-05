punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~0123456789"


def remove_punctuation(string):
    s_sans_punct = ""
    for letter in s:
        if letter in punctuation:
            s_sans_punct += " "
        else:
            s_sans_punct += letter
    return s_sans_punct


count_words(remove_punctuation(s))

def count_words(string):
    wds = string.split()
    x = len(wds)

    return x