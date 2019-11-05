def create_sequence(string, index, length):
    for j in range(index, length):
        if j > len(string)-1:
            j -= len(string)
        else:
            print(string[j], end="")

