def create_sequence(string, index, length):
    empty = ''

    while index <= 0:
        index = index + len(string)

    i = 0

    while i < int(length):
        if index == len(string):
            index -= len(string)
        else:
            empty += string[index]
            index += 1
            i += 1

    return empty
    
