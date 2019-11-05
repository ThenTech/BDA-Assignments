def create_sequence(string, index, lenght):
    while index < 0:
        index += len(string)
    while index > len(string):
        index -= len(string)
    uitkomst = string[index:(index+lenght)]
    index -= (len(string)-len(uitkomst))
    while len(uitkomst) != lenght:
        while index < 0:
            index += len(string)
        while index > (len(string)-1):
            index -= len(string)
        uitkomst += string[index]
        index += 1
    return uitkomst