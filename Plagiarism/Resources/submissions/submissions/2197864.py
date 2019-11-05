def replace(pattern, replacement, corpus):
    niet = ''',?;.:/"<>[]^!'“”’ '''
    teller = 0
    for i in corpus:
        if i == pattern[0]:
            if corpus[teller+1] == pattern[1]:
                if corpus[teller+2] == pattern[2]:
                    nieuwe = corpus[:teller] + replacement + corpus[teller+len(pattern):]
                    return nieuwe
        else:
            teller += 1