def create_sequence(string, index, length):
    output = ""
    substring = ""
    for i in range(len(string)):
        output += string[i]
    for i in range(length - len(string)):
        output += output[i]
    substring = output[index + 1:]
    output = substring + output
    output = output[:index]
    return output





print(create_sequence("word", -5, 15))
