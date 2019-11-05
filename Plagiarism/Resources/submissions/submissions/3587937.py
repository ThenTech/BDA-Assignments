def char_at_index(string, index):
    i = index % len(string)
    return string[i]

def create_sequence(string, start_index, length):
    sequence = ""
    for i in range(start_index, start_index + length):
        char = char_at_index(string, i)
        sequence += char

    return sequence