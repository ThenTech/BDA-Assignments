def count_words(string):
    alphastring = "abcdefghijklmnopqrstuvwxyz"
    wordcount = 0
    lettercount = 0
    inWord = False
    
    for i in string:
            if i in alphastring and not inWord:
                inWord = True
                lettercount += 1
            elif (i not in alphastring and inWord and lettercount >= 2) or (i == string[len(string) - 1] and inWord):
                wordcount += 1
                lettercount = 0
                inWord = False
            elif i in alphastring and inWord: 
                lettercount += 1
    return wordcount
    pass