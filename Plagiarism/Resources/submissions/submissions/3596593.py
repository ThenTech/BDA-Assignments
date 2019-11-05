def create_sequence(string, index, length):
    while (index < 0):
        index += len(string)
    while (index > len(string)):
        index -= len(string)
    x = 0
    print(')
    while(x < length):
        print(string[index], end="")
        x += 1
        index += 1
        if (index > len(string)-1):
            index = 0
    print(')