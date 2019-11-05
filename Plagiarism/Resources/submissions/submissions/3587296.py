import string
def create_sequence(string, index, length):

    while (index < 0):
        index += len(string)
    while (index>len(string)):
        index -=len(string)
    c=(len(string)-index)
    a= (length-c)//len(string)
    b= length-(a*len(string)+c)
    test = string[index:]+a*string[:]+string[:b]
    return test