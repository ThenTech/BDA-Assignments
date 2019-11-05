def replace(pattern, replacement, corpus):
    i = 0
    while i < len(corpus):
        returnword = ""  
        wordfound = True
        for characters in range(len(pattern)):
            if pattern[characters] == corpus[i] and characters == 0:
                start = i
                i += 1
            elif pattern[characters] == corpus[i] and characters == len(pattern)-1:
                break
            elif not pattern[characters] == corpus[i]:
                wordfound = False
                i += 1
                break
            elif pattern[characters] == corpus[i]:
                i += 1
        if wordfound:
            for letter in range(0, start):
                returnword += corpus[letter]
            returnword += replacement
            for letter in range(start+len(pattern), len(corpus)):
                returnword += corpus[letter]
            corpus = returnword
            
            
    return corpus
 