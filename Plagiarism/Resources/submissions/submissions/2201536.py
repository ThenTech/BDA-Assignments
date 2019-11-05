def replace(pattern, replacement, corpus):
    lengtec = len(corpus)
    lengtep = len(pattern)
    
    for i in range (0, lengtec-lengtep):
        for j in range (0, lengtep):
            if corpus[i+j-1] != pattern[j]:
                break
            if j == lengtep-1:
                corpus = corpus[0:i-1] + replacement + corpus[i+j:lengtec]
    return corpus
            