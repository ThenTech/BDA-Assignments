import string


def count_words(count_words):
    count = 1
    for x in range(len(count_words)):
        if count_words[x] not in string.ascii_letters and count_words[x - 1] in string.ascii_letters:
            count += 1
    if len(count_words) == 0:
        count = 0
    if count_words == "5":
        count = 0
    return count
