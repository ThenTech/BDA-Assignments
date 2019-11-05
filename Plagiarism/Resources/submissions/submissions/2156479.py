def create_sequence(string, index, length):
    result = ""
    for i in range(index, index+length):
        result += string[i%len(string)]
    return result