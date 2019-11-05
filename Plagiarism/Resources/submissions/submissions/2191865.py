import string

def count_words(string):
    split_string = string.split
    x = 0
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in string:
            if i == " " or i == "," or i == number:
                x += 1
    return x+1