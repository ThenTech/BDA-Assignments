ef count_words(string):
    alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    counter = 0
    vorige = ""
    for i in string:
        if i not in alfabet and vorige in alfabet:
            counter += 1
        elif i in alfabet:
            vorige = i
    if string[len(string)-1] in alfabet:
        counter += 1

    return counter