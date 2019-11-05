def count_words(sentence):
    sentencewithoutpunc = ""
    for char in sentence:
        if char in """0123456789!\#$%&'()"*+,-./:;<=>?@[\]^_`{|}~':""":
            sentencewithoutpunc += " "
        else:
            sentencewithoutpunc += char

    splitsentence = sentencewithoutpunc.split()
    return len(splitsentence)