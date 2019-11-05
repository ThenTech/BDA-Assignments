def create_sequence(string, index, length):
    result = ""
    for i in range(length):
        if index<0:
            result += string[-index%len(string)]
        else:
            result += string[index%len(string)]
        index += 1
    return result