def write_words(string):
    tempString = ""
    stringLength = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in string:
        if (i.lower() in alphabet):
            tempString += i
            stringLength += 1
        else:
            print(tempString, stringLength, sep=" ")
            tempString = ""
            stringLength = 0