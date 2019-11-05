def create_sequence(string, index, length):
    for i in range(index, index + length):
        x = str(print(string[i % len(string)], end=""))
        return x
