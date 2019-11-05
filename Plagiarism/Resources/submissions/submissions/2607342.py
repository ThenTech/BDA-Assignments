def each_char(index, string):
    i = index % len(string)
    return string[i]


def create_sequence(string, index, length):
    word = ""
    for i in range(index, index + length):
        word += each_char(i, string)
    return word
