def replace(pattern, replacement, corpus):
    i = 0
    while i < len(corpus):
        for characters in range(len(pattern)-1):
            if pattern[characters] == corpus[i]:
                if characters == 0:
                    start = i
                i += 1
            if pattern[characters] != corpus[i]:
                break
            
               
    returnword = ""           
    for letter in range(0, i):
        returnword += corpus[letter]
  
    returnword += replacement
    for letter in range(i+len(pattern)+1, len(corpus)-1):
        returnword += corpus[letter]

        
        
        
    
        