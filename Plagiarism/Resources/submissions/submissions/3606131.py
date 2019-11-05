# write your code here
def listmaker(string):
    alphabetstring = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    inWord = False
    lettercount = 0
    first_letter = 0
    wordlist = []
    
    
    for i in range (len(string)):
        if string[i] in alphabetstring and not inWord:
            inWord = True
            lettercount += 1
            first_letter = i
            continue
        elif (string[i] not in alphabetstring and inWord and lettercount >= 1) or (i == len(string) - 1 and inWord and lettercount >= 1):
            wordlist.append(string[first_letter:i])
            wordlist.append(lettercount)
            lettercount = 0
            inWord = False
            continue
        elif string[i] in alphabetstring and inWord:
            lettercount += 1
            continue
        else:
            continue
    return wordlist
    
sentence = input("Give me a sentence")
woordjes = listmaker(sentence)
i = 0
    
while i < len(woordjes) - 2:
    print(woordjes[i], woordjes[i+1], sep=" ")
    i += 2
        
            