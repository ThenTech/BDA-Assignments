def create_sequence(string, index, length):
    sequence = ""
    k = 1
    while k <= length:
        if index >= len(string) or index <= -(len(string)):
            index = index % len(string)
        sequence += string[index]
        index += 1
        k +=1
    return sequence
