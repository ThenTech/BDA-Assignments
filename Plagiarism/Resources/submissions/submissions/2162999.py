def create_sequence(string, index, length):
    total = ""
    begin = index % len(string)
    if begin < 0:
        begin2 = begin + len(string)
    else:
        begin2 = begin
    full_string = (string * (length//len(string) + 2))
    for i in range(begin2, begin + length):
        total += full_string[i]
    return total