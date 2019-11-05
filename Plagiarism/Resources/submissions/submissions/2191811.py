import string

def count_words(string):
    split_string = string.split
    x = 0
    number = "0123456789"
    for i in string:
        if i == " " or i == "," or i == number:
            x += 1
    return (x+1)
