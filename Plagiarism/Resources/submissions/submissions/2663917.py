def char_at(string, index):
    i = index % len(string)
    return string[i]


def create_sequence(string, index, length):
    result = ""
    for i in range(index, index + length):
        result += char_at(string, i)
    return result

