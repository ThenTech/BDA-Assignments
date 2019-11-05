def create_sequence(string, index, length):
    result = ''
    for i in range(length):
        result += string[((index % len(string)) + i)]
        
    return result