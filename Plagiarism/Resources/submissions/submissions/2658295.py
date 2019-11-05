def find_first_letter(string, n):
    while len(string)*2 > n:
        n += len(string)
    while len(string)*2 < n:
        n -= len(string)
    return n

def create_sequence(string, index, length):
    index = find_first_letter(string, index)
    for i in string:
        string = string + str(i)
    sequence = ""
    sequence = string[index:]
    x = len(sequence)
    if x > int(length):
        length += x
    y = True
    while y:
        for i in string:
            x = len(sequence)
            if x == length:
                y = False
                break            
            sequence = sequence + i
    return sequence