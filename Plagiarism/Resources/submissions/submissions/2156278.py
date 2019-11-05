def create_sequence(string, index, length):
    sequence = ""
    for x in range(index, index + length):
        y = x
        while 0 > x <len(string):
            y = x + len(string)
        sequence+= string[y]
    return sequence