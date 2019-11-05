def create_sequence(string, index, length):
    sequence = ""
    for i in range(index, index + length):
        sequence += string[i % len(string)]
    print(sequence)