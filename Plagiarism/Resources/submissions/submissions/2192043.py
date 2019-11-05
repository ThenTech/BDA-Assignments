def count_words(ss):
    numbers = "0123456789"
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    cleanstring = ""
    for letter in ss:
        if letter not in punctuation and letter not in numbers:
            cleanstring += letter
        else:
            cleanstring += " "
    #print(cleanstring)

    wds = cleanstring.split()
    x = len(wds)
    return x
    