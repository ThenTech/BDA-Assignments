def create_sequence(string, index, length):
    x = ""
    for i in range(index, index + length):
        x += string[i % len(string)]
    return x