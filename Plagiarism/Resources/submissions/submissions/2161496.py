def create_sequence(string, index, length):

    while 0 < index < len(string)-1:
        index += len(string)
    word = ""
    for i in range(len(word) < int(length)):
        x = i % len(string)
        print(i)
        word += string[i + index]
    return word