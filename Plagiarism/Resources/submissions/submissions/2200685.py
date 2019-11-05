def replace(pattern, replacement, corpus):
    x = 0
    if pattern not in corpus:
        return corpus
    else:
        while x < len(corpus):
            if corpus[x:x+len(pattern)] == pattern:
                corpus = corpus[:x] + corpus[x + len(pattern):]
                corpus = corpus[:x] + replacement + corpus[x:]
            x += 1
        return corpus
replace("is", "was", "This is an example!")