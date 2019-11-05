def replace(pattern, replacement, corpus):
    a = startingPosition(pattern, corpus)
    tempString = ""
    while (a != -1):
        for i in range(len(corpus)):
            if (i == a or (i > a and (i - a) < len(replacement)+1)):
                tempString += replacement[i-a]
            else:
                tempString += corpus[i]
        a = startingPosition(pattern, tempString)
        corpus = tempString
        tempString = ""
        
    return tempString

def startingPosition(pattern, corpus):
    startingPos = 0
    
    patternLetterPos = 0
    for i in range(len(corpus)):
        if patternLetterPos != len(pattern):
            if corpus[i] == pattern[patternLetterPos] and patternLetterPos == 0:
                startingPos = i
                patternLetterPos += 1
    
            elif corpus[i] != pattern[patternLetterPos]:
                startingPos = 0
                patternLetterPos = 0
                
            elif corpus[i] == pattern[patternLetterPos]:
                patternLetterPos += 1
    
        else:
            return startingPos
    
    return -1