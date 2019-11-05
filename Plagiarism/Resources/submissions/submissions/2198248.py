def replace(pattern, replacement, corpus):
    teller = 0
    teller2 = 0
    for i in corpus:
        if i == pattern[0]:
            if corpus[teller+1] == pattern[1]:
                nieuwe = corpus[:teller] + replacement + corpus[teller+len(pattern):]
                for j in corpus[teller+len(pattern):]:
                    if j == pattern[0]:
                        if corpus[teller2 + 1] == pattern[1]:
                            nieuwe = corpus[:teller] + replacement + corpus[teller + len(pattern): teller2] + replacement + corpus[teller2 + len(pattern)]
                    else:
                        teller2 += 1
        else:
            teller += 1
    if teller == len(corpus):
        return corpus
    else:
        return nieuwe