def create_sequence(string, index, length):
    for i in range(index, index + length):
        return string[i % len(string)]
    