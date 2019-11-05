def create_sequence(string, index, length):
    result = ''
    for i in range(length - 1):
        result += string[index % strlen(string) + i]
        
    return result