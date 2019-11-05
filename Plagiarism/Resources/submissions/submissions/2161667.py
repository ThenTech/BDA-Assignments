def create_sequence(string, index, length):
    for x in range(length):
        print(string[index], end='')
        index += 1
        if index == (len(string)):
            index = 0
create_sequence("word", -3, 9)