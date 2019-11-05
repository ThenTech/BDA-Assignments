letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def remove(zin):
    new_string = ""
    for i in zin:
        if i in letters:
            new_string += i
        elif i == " ":
            new_string += " "
        else:
            continue
    return new_string
def cleanup_spaces(s):
    new_word = ""
    new_sentence = remove(s).split()
    for i in new_sentence:
        new_word += (i + " ")
    return new_word