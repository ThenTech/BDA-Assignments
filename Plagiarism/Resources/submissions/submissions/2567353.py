def create_sequence(string, index, length):
    x = ''
    for i in range(length):
        x = x + stirng[(index + i)%(len(string))]
    return x