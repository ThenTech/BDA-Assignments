def create_sequence(string, index, length):
    for i in range(index, length + index):
        print(string[i % len(string)], end="")
    pass