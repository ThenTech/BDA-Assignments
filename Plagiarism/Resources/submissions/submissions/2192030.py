import string

numbers = "123456789"
def count_words(zin):
    new_string = ""
    for i in zin:
        if i in string.punctuation:
            new_string += " "
        elif i in numbers:
            new_string += " "
        else:
            new_string += i
    words = new_string.split()
    return len(words)