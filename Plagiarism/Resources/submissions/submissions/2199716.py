def create_sequence(string, index, length):
    result = ""
    for i in range(length//len(string)+1):
        if index<0:
            result += string[len(string)-index%len(string)]
        else:
            result += string[index%len(string)]
        index += 1
    print(result)