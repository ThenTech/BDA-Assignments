def replace(pattern, replacement, corpus):
    for i in range(len(corpus)):
        place = 0
        while corpus[i+place] == pattern[place]:
            if place == len(pattern)-1:
                corpus = corpus[:i-place] + replacement + corpus[i:]
            else:
                place += 1
    return corpus