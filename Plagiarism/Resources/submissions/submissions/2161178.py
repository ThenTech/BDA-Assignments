def create_sequence(string, index, length):
    output = string * length
    output = output[index:]
    for i in enumerate(range(length)):
        output += string
    output = output[:-4 * length]
    return output



print(create_sequence("word", 0, 4))
