def remove_punc(string):
    word = ""
    for i in string:
        if i not in "123456890,!":
            word += i
        else:
            word += " "
    return word


def count_words(string):
    x = remove_punc(string)
    z = x.split()
    return len(z)