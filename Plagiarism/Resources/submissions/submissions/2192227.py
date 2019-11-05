s = input()

def count(s):
    numbers = "0123456789"
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    cleanstring = ""
    for letter in s:
        if letter not in punctuation and letter not in numbers:
            cleanstring += letter
        else:
            cleanstring += " "
    #print(cleanstring)

    wds = cleanstring.split()
    #print(wds)
    l = len(wds)
    for i in range(0,l):
        #output = ""
        print(wds[i], end=" ")
        print(len(wds[i]))
        #print(output)

count(s)