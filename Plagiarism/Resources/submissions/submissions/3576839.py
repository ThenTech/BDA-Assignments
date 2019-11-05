def create_sequence(string, index, length):
    while index < 0:
        index += len(string)
    
    output = ""
    for i in range(length):
        place = index + i
        while place >= len(string):
            place -= len(string)
        output += string[place]
    return output
        