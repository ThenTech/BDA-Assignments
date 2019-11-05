def create_sequence(string, index, length):
    word = ""
    while index < 0:
        index += len(string)
    while index >= len(string):
        index -= len(string)

    while len(word) <= length-1:
        if index > len(string)-1:
            index -= len(string)
        else:
            word += string[index]
            index += 1
    return word

    
