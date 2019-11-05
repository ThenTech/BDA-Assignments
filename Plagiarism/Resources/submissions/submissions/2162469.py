def create_sequence(string, index, length):
    while index < 0 and index < len(string)-1:
        index += len(string)
        print(index)
    while index > len(string)-1 and index > 0:
        index -= len(string)
        print(index)
    word = ""
    check = len(word)
    firstch = len(string)
    while check < length:
        check = len(word)
        if index >= 0 and index <= len(string)-1:
            word = word + string[index]
            index += 1
        else:
            index -= firstch
    return word