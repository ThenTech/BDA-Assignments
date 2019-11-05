def create_sequence(string, index, length):
    while(index<0):
        index+=len(string)

    for i in range(length):
        j=i+index
        j=j%len(string)
        print(string[j], end="")