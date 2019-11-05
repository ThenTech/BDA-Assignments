uitkomst = ''
def create_sequence(string, index, length):
    for x in range(length):
        global uitkomst
        uitkomst += str(string[index])
        index += 1
        if index == (len(string)):
            index = 0

print(str(uitkomst))