def replace(pattern, replacement, corpus):
    i = 0
    
    while i < len(corpus):
        print(len(corpus))
        i += 1
        place = 0
        while corpus[i+place] == pattern[place]:
            if place == len(pattern)-1:
                corpus = corpus[:i] + replacement + corpus[i+place+1:]
                i += place
                break
            else:
                place += 1
                if i + place >= len(corpus):
                    break
    return corpus