import string


def count_words(count_words):
    count = 1
    for x in range(len(count_words)):
        if count_words[x] not in string.ascii_letters and count_words[x - 1] in string.ascii_letters:
            count += 1
    return count
