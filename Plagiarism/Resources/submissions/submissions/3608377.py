def create_sequence(string, index, length):
    result = ''
    for i in range(length - 1):
        result += string[index % len(string) + i]
        
    return result