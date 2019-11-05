def count_words(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    amount = 0
    in_alphabet = False
    boolean = False
    for i in string:
        for j in alphabet:
            if i == j:
                in_alphabet = True
        if in_alphabet:
            if not(boolean):
                amount +=1
                boolean = True
        else:
            boolean = False
        in_alphabet = False
    return amount