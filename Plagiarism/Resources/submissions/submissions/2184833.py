def create_sequence(string, index, length):
    word = ""
    for j in range(index, length):
        if j > len(string)-1:
            j -= len(string)
        else:
            word += string[j]
    return word
    
