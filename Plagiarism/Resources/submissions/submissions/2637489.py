def create_sequence(string, index, length):
    new_word = ""
    for i in range(index, length + index):
        new_word += string[i % len(string)]
    return new_word