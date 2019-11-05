def count_words(string):
    alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counter = 0
    vorige = ""
    for i in string:
        if i not in alfabet and vorige in alfabet:
            counter += 1
            vorige = i
        elif i in alfabet:
            vorige = i
    if vorige in alfabet:
        counter += 1

    return counter