import string


def count_words(s):
    numbers = "1234567890"
    for letter in s:
        if letter in string.punctuation:
            s = s.replace(letter, " ")
    for letter in s:
        if letter in numbers:
            s = s.replace(letter, " ")
    return len(s.split())
