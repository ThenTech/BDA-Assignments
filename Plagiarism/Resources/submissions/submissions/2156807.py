def create_sequence(string, index, length):
    sequence = ""
    z = index
    for x in range(length):
        while not(0 <= z < len(string)) :
            if z < 0:
                z += len(string)
            elif z >= len(string):
                z -= len(string)

        sequence+= string[z]
        z = index + x +1

    return sequence