def replace(pattern, replacement, corpus):
    while (startingPosition(pattern, corpus) != -1):
        

def startingPosition(pattern, corpus):
    startingPos = 0
    patternLetterPos = 0
    for i in range(len(corpus)):
        if patternLetterPos != len(patternLetterPos):
            if  corpus[i] == pattern[patternLetterPos] and patternLetterPos = 0:
                startingPos = i
                
            elif corpus[i] != pattern[patternLetterPos]:
                startingPos = 0
                patternLetterPos = 0

        else:
            return patternLetterPos
            
        patternLetterPos += 1
    return -1
            
            
        