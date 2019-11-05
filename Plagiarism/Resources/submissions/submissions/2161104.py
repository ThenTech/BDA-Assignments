def create_sequence(string, index, length):
    word = ""
    while index > (len(string)-1):
        index -= len(string)
    for i in range(length):
        if index < (len(string)-1):
            word += string[index]
            index += 1
        else:
            index -= len(string)
            word += string[index]
    return word