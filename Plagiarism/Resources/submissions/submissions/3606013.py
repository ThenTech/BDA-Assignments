def count_words(string):
    alphastring = "abcdefghijklmnopqrstuvwxyz"
    wordcount = 0
    lettercount = 0
    inWord = False
    
    for i in string:
        for j in alphastring:
            if i == j and not inWord:
                inWord = True
                lettercount += 1
                break
            elif (i not in alphastring and inWord and lettercount >= 2) or i == string[len(string) - 1] :
                wordcount += 1
                lettercount = 0
                inWord = False
                break
            elif i == j and inWord: 
                lettercount += 1
                continue
    return wordcount
    pass