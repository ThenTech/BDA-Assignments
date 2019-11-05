import string


def is_palindrome_sentence(sentence):
    sentence1 = ""
    sentence2 = ""
    for letter in sentence:
        if letter in string.ascii_letters:
            sentence1 += letter
    for x in range(len(sentence1)):
        sentence2 += sentence1[len(sentence1) - x - 1]
    sentence1 = sentence1.lower()
    sentence2 = sentence2.lower()
    if sentence2 == sentence1:
        return True
    else:
        return False
