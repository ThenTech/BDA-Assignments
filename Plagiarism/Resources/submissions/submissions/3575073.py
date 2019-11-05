def replace(pattern, replacement, corpus):
    for i in range(len(corpus)):
        place = 0
        while corpus[i+place] == pattern[place]:
            if place == len(pattern)-1:
                corpus = corpus[:i] + replacement + corpus[i+place:]
                break
            else:
                place += 1
                if i + place >= len(corpus):
                    break
    return corpus