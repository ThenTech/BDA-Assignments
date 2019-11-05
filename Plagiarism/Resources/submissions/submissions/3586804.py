def create_sequence(string, index, length):
    letter = ""
    for i in range(index, length+index):
        number = i % len(string)
        letter += string[number]
    return letter

print(create_sequence("word", -3, 9))