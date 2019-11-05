def count_words(string):
    alphabet = ["abcdefghijklmnopqrstuvwxyz"]
    amount = 0
    boolean = False
    for counter in [0, len(string) - 1]:
        if string[counter] == alphabet:
            boolean == True
            continue
        else:
            if boolean == True:
                amount += 1
                boolean = False
                continue
            else:
                continue