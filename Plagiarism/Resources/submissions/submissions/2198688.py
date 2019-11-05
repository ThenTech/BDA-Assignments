import string


def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct
    
def is_palindrome_sentence(sentence):
    is_palindrome = True
    sentence = remove_punctuation(sentence)
    sentence = sentence.lower()
    sentence = sentence.replace(" ", "")
    senLen = len(sentence)
    counter = -1
    for i in range(senLen - 1):
        if sentence[i] != sentence[counter]:
            is_palindrome = False
            break
        else:
            counter -= 1
    return is_palindrome