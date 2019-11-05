import string

def count_words(string):
    split_string = string.split
    x = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789,!"
    for i in string:
            if i not in alphabet:
                x += 1
    return x+1