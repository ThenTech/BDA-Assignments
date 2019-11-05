def caracter(string, index):
    i = index % len(string)
    return string[i]


def write_sequence(string, index, length):
    for i in range(index, index + length):
        print(caracter(string, i), end="")
    print()
    

write_sequence("word", -3, 9)
write_sequence("word", -5, 15)