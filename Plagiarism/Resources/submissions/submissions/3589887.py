def replace(pattern, replacement, corpus):
    position = 0
    patternLooper = 0
    newString = ""
    for i in range(len(corpus)):
        if pattern[0] == corpus[i]:
            position = i
            patternLooper += 1
        elif pattern[patternLooper] != corpus[i]:
            if corpus[i] != " " and position != 0 and patternLooper == 1:
                newString += corpus[i-1]
            position = 0
            patternLooper = 0
            newString += corpus[i]
        elif pattern[len(pattern)-1] == corpus[i]:
            for i in range(len(pattern)):
                if i < len(replacement):
                    newString += replacement[i]

        elif pattern[patternLooper] == corpus[i]:
            patternLooper += 1
        else:
            newString += corpus[i]
            
replace("with", "for", "I play with a sentence without words")