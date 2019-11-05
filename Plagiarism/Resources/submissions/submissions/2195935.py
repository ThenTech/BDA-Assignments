punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~0123456789"

def remove_punctuation(s):

    s_sans_punct = ""
    for letter in s:
        if letter not in punctuation:
            s_sans_punct += letter
        else:
            s_sans_punct += " "
    return s_sans_punct

def count_words(s):

    zonder_dinges = remove_punctuation(s).split()
    aantal_woorden = len(zonder_dinges)
    return aantal_woorden

count_words(s)