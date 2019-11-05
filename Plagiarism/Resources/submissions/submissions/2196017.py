import string


def count_words(s):
    s_without_punct = ""
    s_without_numbers = ""
    numbers = "123456789"
    s_without_punct = s.translate(s.maketrans(string.punctuation, " "*len(string.punctuation)))
    for letters in s_without_punct:
        if letters not in numbers:
            s_without_numbers += letters
    xs = s_without_numbers.split()
    return len(xs)