def create_sequence(string, index, length):
    total = ""
    begin = index % len(string)
    if begin < 0:
        begin += len(string)
    full_string = (string * (length//len(string) + 1))
    for i in range(begin, begin + length):
        total = total + full_string[i]
    return total