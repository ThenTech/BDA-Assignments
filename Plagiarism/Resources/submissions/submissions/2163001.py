def create_sequence(string, index, length):
    output = ""
    z = index
    for i in range(length):
        while not 0 <= z < len(string):
            if z < 0:
                z += len(string)
            elif z >= len(string):
                z -= len(string)

        output += string[z]
        z = index + i + 1
    return output