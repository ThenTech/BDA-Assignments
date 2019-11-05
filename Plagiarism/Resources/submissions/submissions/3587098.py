def replace(pattern, replacement, corpus):
    a = startingPosition(pattern, corpus)
    tempString = ""
    while (a != -1):
        for i in range(len(corpus)):
            if (i == a):
                tempString += replacement
                i += len(replacement)
            else:
                tempString += corpus[i]
        a = startingPosition(pattern, corpus)

def startingPosition(pattern, corpus):
    startingPos = 0
    
    patternLetterPos = 0
    for i in range(len(corpus)):
        if patternLetterPos != len(pattern):
            if corpus[i] == pattern[patternLetterPos] and patternLetterPos == 0:
                startingPos = i
    
            elif corpus[i] != pattern[patternLetterPos]:
                startingPos = 0
                patternLetterPos = 0
    
        else:
            return startingPos
    
        patternLetterPos += 1
    return -1