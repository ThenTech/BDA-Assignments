sentence = str(input("string:"))
punctuation = "“!\"”#$%&'()*+,-./:;<=>?@[]^_`{|}~0123456789 "
def remove_punctuation(sentence):

    s_sans_punct = ""
    for letter in sentence:
        if letter not in punctuation:
            s_sans_punct += letter
        else:
            s_sans_punct += " "
    return s_sans_punct

new_sentence = remove_punctuation(sentence)
lijst = new_sentence.split()
for word in lijst:
    print(word, len(word))