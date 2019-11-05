def remove_punctuation(s):
    sentence_without_punct = ""
    for letter in s:
        if letter not in """0123456789!\#$%&'()"*+,-./:;<=>?@[\]^_`{|}~':""":
            sentence_without_punct += letter
    return sentence_without_punct


def count_words(sentence):
    x = remove_punctuation(sentence)

    splitsentence = x.split()
    print(len(splitsentence))




count_words("ik heb honger,hallo1slaap 51")

