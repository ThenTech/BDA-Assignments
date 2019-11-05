def create_sequence(string, index, length):
    result = ""
    for i in range(length):
        if index<0:
            huidige = len(string)+index%len(string)
            result += string[len(huidige)]
        else:
            result += string[index%len(string)]
        index += 1
    return result

create_sequence("word", -3, 9)