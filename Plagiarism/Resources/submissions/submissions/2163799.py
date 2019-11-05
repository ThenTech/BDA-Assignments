def create_sequence(string, index, length):
    for i in range(index, index + length):
        x = print(string[i % len(string)], end="")
    return str(x)