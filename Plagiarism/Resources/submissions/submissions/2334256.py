def count_words(s):
    counter = 1
    if return_word(s):
        counter += 1
    return counter


def return_word(s):
    word = ""
    for ch in s:
        if "a" <= ch <= "z" or "A" <= ch <= "Z":
            word += ch
        else:
            return word
    return word
