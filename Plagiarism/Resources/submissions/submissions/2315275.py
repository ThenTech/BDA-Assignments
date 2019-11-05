def count_words(string):
    amount = 0
    word = False
    for c in string:
        if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
            if(word == False):
                amount += 1
                word = True
        else:
            word = False
    return amount
        