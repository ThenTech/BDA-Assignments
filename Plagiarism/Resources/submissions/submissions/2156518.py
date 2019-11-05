def create_sequence(string, index, length):
    sequence = ""
    y = index
    z = 0
    for x in range(length):
        while 0 > z <len(string):
            if y < 0:
                z += len(string)
            elif y > len(string):
                z -= len(string)
            else:
                z = y
        sequence+= string[z]
        y +=1

    return sequence
