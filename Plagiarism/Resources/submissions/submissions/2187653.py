def create_sequence(string, index, length):
    uitkomst = ''
    for x in range(length):
        
        if index != (len(string)):
            if len(string) > index >=0:
                uitkomst += str(string[index])
                index += 1

            elif index < 0:
                index += len(string)
            else:
                index = index - len(string)
        if index == (len(string)):
            index = 0
    return uitkomst
print(create_sequence("word", -3, 9))