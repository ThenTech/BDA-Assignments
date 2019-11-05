def create_sequence(string, index, length):
    sequence = ""
    for x in range(index, index + length):
        y = x
        while 0 > y <len(string):
            y += len(string)
            
        sequence+= string[y]
    return sequence