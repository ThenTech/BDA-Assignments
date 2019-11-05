def count_words(string):
    stringArray = []
    i = 0
    while len(string) > 0:
        if not isvalidchar(string[i]):
            if i > 0:
                stringArray.append(string[0:i])
            string = string[i+1:len(string)]
            i = 0
        else:
            if i < len(string) - 1:
                i += 1
            else:
                if i > 0:
                    stringArray.append(string[0:len(string)])
                string = string[i+1:len(string)]
                i = 0
    return len(stringArray)

def isvalidchar(character):
    validchars = "abcdefghijklmnopqrstuvwxyz"
    valid = False
    for i in range(0, len(validchars)):
        if character == validchars[i]:
            valid = True
            break
    return valid

count_words("five 6 seven,eight!nine")