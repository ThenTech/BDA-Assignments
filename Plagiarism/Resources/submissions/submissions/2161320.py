def create_sequence(string, index, length):
    word = ""
    if index > 0:
        while index > (len(string)-1):
            index -= len(string)
    else:
        while index < 0:
            index += len(string)
    for i in range(length):
        if index < (len(string)):
            word += string[index]
            index += 1
        else:
            index -= len(string)
            word += string[index]
            index += 1
    return word