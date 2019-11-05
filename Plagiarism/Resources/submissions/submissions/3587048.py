def string(input):
    tempString = ""
    stringLength = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in input:
        if (i.lower() in alphabet):
            tempString += i
            stringLength += 1
        else:
            print(tempString, stringLength, sep=" ")
            tempString = ""
            stringLength = 0
            
string(input("Give an input: "))