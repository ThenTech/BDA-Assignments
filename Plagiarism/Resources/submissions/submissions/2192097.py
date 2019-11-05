def count_words(string):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    counter = 0

    for i in string:
        if i not in alfabet:
            counter += 1
    if string[len(string)-1] in alfabet:
        counter += 1

    return counter