def replace(pattern, replacement, corpus):
    i = 0
    while i < len(corpus):
        for characters in range(len(pattern)):
            if pattern[characters] == corpus[i]:
                if characters == 0:
                    start = i
                i += 1
            if pattern[characters] != corpus[i]:
                i += 1
                break
            
               
    returnword = ""           
    for letter in range(0, start):
        returnword += corpus[letter]
  
    returnword += replacement
    for letter in range(start+len(pattern), len(corpus)):
        returnword += corpus[letter]

    return returnword
        