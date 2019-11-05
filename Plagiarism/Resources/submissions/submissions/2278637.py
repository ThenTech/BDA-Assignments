def caracter(string, index):
    i = index % len(string)
    return string[i]


def create_sequence(string, index, length):
    for i in range(index, index + length):
        print(caracter(string, i), end="")
    print()
    

create_sequence("word", -3, 9)
create_sequence("word", -5, 15)