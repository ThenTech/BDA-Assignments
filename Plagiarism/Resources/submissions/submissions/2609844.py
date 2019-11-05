def create_sequence(string, index, length):
    new = ""
    for i in range(index,index+length):
        m = i % len(string)
        new += string[m]
    return new
        