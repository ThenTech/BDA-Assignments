def count_words(string):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    spatie = False
    words = 0
    for i in string:
        if i not in alfabet and spatie:
            spatie = False
            words += 1
        elif i not in alfabet and not spatie:
            continue
        else:
            spatie = True
    if spatie:
        words += 1
    return words
