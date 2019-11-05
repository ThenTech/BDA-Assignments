import string


def count_words(count_words):
    count = 1
    for letter in count_words:
        if letter in string.punctuation:
            count += 1
    return count