def create_sequence(string, index, length):
    output = ""
    for i in range(index, index + length):
        output += string[i % len(string)]
    return output
