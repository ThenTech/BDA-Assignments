def create_sequence(string, index, length):
    index = index % len(string)
    result = ""
    for i in range(length):
        if index == len(string) - 1:
            index = 0
        elif i != 0:
            index = index + 1
        result += string[index]
    return result