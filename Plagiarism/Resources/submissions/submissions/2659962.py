def lettergeven(string, index):
    i = index % len(string)
    return string[i]
def create_sequence(string, index, length):
    uitkomst = ""
    for i in range(index, index + length)
        uitkomst += lettergeven(string, i)
    return uitkomst