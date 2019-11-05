import string

def count_words(string):
    split_string = string.split
    x = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
            for j in string:
                if j != i:
                    return x+1