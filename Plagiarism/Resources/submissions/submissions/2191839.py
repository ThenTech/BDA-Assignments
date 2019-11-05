def count_words(string):
    alphabet = ["abcdefghijklmnopqrstuvwxyz"]
    amount = 0
    boolean = False
    for counter in [0, len(string) - 1]:
        if string[counter] == alphabet:
            if boolean == False:
                boolean == True
                amount += 1
            continue
        else:
            if boolean == True:
                boolean = False
                continue
            else:
                continue
    return amount