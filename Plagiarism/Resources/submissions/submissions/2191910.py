def count_words(string):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    amount = 0
    boolean = False
    for counter in [0, len(string) - 1]:
        if string[counter] == alphabet:
            if boolean == False:
                boolean = True
                amount += 1
            continue
        else:
            if boolean == True:
                boolean = False
                continue
            else:
                continue
    return amount