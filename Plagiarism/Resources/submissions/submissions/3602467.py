def create_sequence(string, index, length):
    list = []
    for i in range(index, length + index):
        list.append(string[i % len(string)])
    return ''.join(list)
    
    pass