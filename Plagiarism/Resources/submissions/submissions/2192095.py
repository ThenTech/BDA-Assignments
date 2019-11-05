import string


def is_palindrome_sentence(sentence):
    sentence1 = ""
    sentence2 = ""
    for letter in sentence:
        if letter not in string.punctuation:
            sentence1 += letter
    for x in range(len(sentence1),0):
        sentence2 += sentence1[x]
    sentence1.lower()
    sentence2.lower()
    if sentence2 == sentence1:
        return True
    else:
        return False
