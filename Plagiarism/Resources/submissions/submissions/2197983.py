punctuation = "“!\"”#$%&'()*+,-./:;<=>?@[]^_`{|}~0123456789 "

def remove_punctuation(sentence):

    s_sans_punct = ""
    for letter in sentence:
        if letter not in punctuation:
            s_sans_punct += letter
    return s_sans_punct

remove_punctuation(sentence)

def is_palindrome_sentence(sentence):
    n = len(sentence)
    if sentence[0] == sentence[n - 1]:
        for x in range(n):
            if sentence[0 + x] == sentence[n - 1 - x]:
                print("True")
    else:
        print("False")

is_palindrome_sentence(sentence)