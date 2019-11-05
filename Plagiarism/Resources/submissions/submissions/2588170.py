def create_sequence(string, index, length):
    string2 = ""
    for i in range(index, index + length):
        while i < 0 or i >= len(string):
            if i < 0:
                i += len(string)
            if i >= len(string):
                i -= len(string)
        string2 += string[i]
    return (string2)