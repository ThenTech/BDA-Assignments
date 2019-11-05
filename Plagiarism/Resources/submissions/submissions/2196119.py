def count_words(string):
    new_string = ""
    for letter in string:
        if letter not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            new_string += " "
        else: 
            new_string += letter
    return len(new_string.split())