def create_sequence(string, index, length):
    word = ""
    while 0 < index < len(string)-1:
        index += len(string)
    for x in range(int(len(word))<int(length)):
        word += string[x % len(string)]
    
    return word