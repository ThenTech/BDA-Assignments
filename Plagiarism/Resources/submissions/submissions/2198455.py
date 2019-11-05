
punctuation = "“!\"”#$%&'()*+,-./:;<=>?@[]^_`{|}~0123456789 "

def remove_punctuation(sentence):

    s_sans_punct = ""
    for letter in sentence:
        if letter not in punctuation:
            s_sans_punct += letter
    return s_sans_punct



def is_palindrome_sentence(sentence):
    n = len(sentence)
    for x in range(n):
        if sentence[0 + x] == sentence[n - 1 - x]:
            palindrome = True
        else:
            palindrome = False
    if palindrome == True:
        print("True")
    else:
        print("False")
