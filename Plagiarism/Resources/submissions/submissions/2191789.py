import string

def count_words(string):
    split_string = string.split
    x = 0
    for i in string:
        if i == " ":
            x += 1
    print(x+1)
