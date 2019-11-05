def count_words(string):
    stringArray = []
    i = 0
    while len(string) > 0:
        if not isvalidchar(string[i]):
            if i > 0:
                stringArray.append(string[0:i])
            string = string[i+1:len(string)]
            i = 0
        i += 1
    return len(stringArray)

def isvalidchar(character):
    validchars = "abcdefghijklmnopqrstuvwxyz"
    valid = False
    for i in range(0, len(validchars)):
        if character == validchars[i]:
            valid = True
            break
    return valid
