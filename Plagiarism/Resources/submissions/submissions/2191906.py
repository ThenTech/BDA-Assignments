import string


def count_words(count_words):
    count = 1
    for x in range(len(count_words)):
        if x in string.punctuation:
            count += 1
    return count