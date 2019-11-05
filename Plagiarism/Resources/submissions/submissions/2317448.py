def create_sequence(string, index, length):
    word = ""
    if index < 0:
        index += + 2* len(string)
    begin = index % len(string)
    for i in range(length):
        word += string[(begin + i)%len(string)]
    return word

create_sequence("word", -3, 9)