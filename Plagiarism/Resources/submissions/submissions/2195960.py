def replace(pattern, replacement, corpus):
    i = 0
    while i < len(corpus):
        wordfound = True
        for characters in range(len(pattern)):
            if pattern[characters] == corpus[i] and characters == 0:
                start = i
            if not pattern[characters] == corpus[i]:
                wordfound = False
        if wordfound:
            returnword = ""           
            for letter in range(0, start):
                returnword += corpus[letter]
            returnword += replacement
            for letter in range(start+len(pattern), len(corpus)):
                returnword += corpus[letter]
        corpus = returnword
            
    return corpus
        