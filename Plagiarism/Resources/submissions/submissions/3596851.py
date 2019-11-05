def create_sequence(string, index, length):
    str=""
    while (index < 0):
        index += len(string)
    while (index > len(string)):
        index -= len(string)
    x = 0
    if (len(string) == 1):
        index = 0
    while(x < length):
        str += string[index]
        x += 1
        index += 1
        if (index > len(string)-1):
            index = 0
    return str