def is_palindrome_sentence(sentence):
    alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    zin = ""
    for i in sentence:
        if i in alfabet:
            zin += i
        else:
            continue
    zin = zin.lower()
    lijst = []
    for i in zin:
        lijst.append(i)
    return lijst == lijst.reverse()