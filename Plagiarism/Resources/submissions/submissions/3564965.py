def create_sequence(string, index, length):
    for i in range(length):
        if index == len(string) - 1:
            index = 0
        else:
            index = index + 1
        print(string[index], end="")