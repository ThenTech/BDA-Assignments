uitkomst = ''
def create_sequence(string, index, length):
    for x in range(length):
        global uitkomst
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
