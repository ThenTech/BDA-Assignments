def replace(pattern, replacement, corpus):
    new_str = ''
    while corpus.find(pattern) >= 0:
        
        for i in range(corpus.find(pattern)):
            new_str += corpus[i]
            
        for i in replacement:
            new_str += i

        corpus = corpus[corpus.find(pattern)+len(pattern):]

    new_str += corpus
    return new_str