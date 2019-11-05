def create_sequence(string, index, length):
    sequence = ""
    y = index
    for x in range(length):
        z = -1
        while z < 0 or z >= len(string):
            if y < 0:
                z += len(string)
            elif y >= len(string):
                z -= len(string)
            else:
                z = y
        sequence+= string[z]
        y +=1

    return sequence