alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def count_words(string):
    tolist = ""
    for i in string:
        if i in alphabet:
            tolist += i
        else:
            tolist += " "
    tolist = tolist.split()
    output = 0
    for i in tolist:
        output += 1
    return output
