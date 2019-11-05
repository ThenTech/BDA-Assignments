import string


def count_words(s):
    s_without_punct = ""
    s_without_numb = ""
    numbers = "1234567890"
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    for letter in s_without_punct:
        if letter not in numbers:
            s_without_numb += letter
    return len(s_without_numb.split())
