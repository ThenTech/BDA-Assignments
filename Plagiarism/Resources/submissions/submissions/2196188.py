def substring(sentence, index, amount):
    new = ""
    for i in range(amount):
        new += sentence[index+i]
    return new


def find_pos(string1, string2):
    for i in range(len(string2)-len(string1)+1):
        if substring(string2, i, len(string1)) == string1:
            return i


def in_string(string1, string2):
    return not (find_pos(string1, string2)) == None
