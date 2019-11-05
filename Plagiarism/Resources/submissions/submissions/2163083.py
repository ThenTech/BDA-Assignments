def create_sequence(string, index, length):
    output = ""
    plusIndex = 0
    for i in range(index, index + length):
        if i < 0:
            test = i
            while test < -len(string):
                test += len(string)
            newString = ""
            for j in range(len(string)):
                newString += string[len(string) - 1 - j]
            output += newString[(-test)-1]
        elif i > len(string) - 1:
            output += string[plusIndex]
            if plusIndex == len(string) - 1:
                plusIndex = 0
            else:
                plusIndex += 1
        else:
            output += string[i]
    return output