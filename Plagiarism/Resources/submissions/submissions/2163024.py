def create_sequence(string, index, length):
    total = ""
    begin = index % len(string)
    full_string = (string * (length//len(string) + 2))
    for i in range(begin, begin + length):
        total += full_string[i]
    return total