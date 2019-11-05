alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def count_words(string):
    words=1
    i=0
    while i != len(string):
        while string[i] in alfabet:
            i+=1
            if i == len(string):
                return words
        words+=1
        i+=1
    return words