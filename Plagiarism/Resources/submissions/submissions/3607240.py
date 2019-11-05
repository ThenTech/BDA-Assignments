def create_sequence(string, index, length):
    while index < len(string):
        index += len(string)
    while index > len(string):
        index -= len(string)
    
    output = ""
    for i in range(length):
        if i + index > len(string):
            index -= len(string)
        output += string[index+i]
    return output