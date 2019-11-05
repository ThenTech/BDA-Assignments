def create_sequence(string, index, length):
    outWord = ""

    for i in range(0, length):
        outWord += string[index % len(string)]
        index += 1
    return outWord
