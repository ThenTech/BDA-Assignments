def replace(pattern, replacement, corpus):
    plaats = []
    count = 0
    for i in range(len(corpus)):
        if corpus[i] == pattern[0]:
            for j in range(len(pattern)):
                if corpus[i+j] == pattern[j]:
                    count += 1
            if count == len(pattern):
                plaats.append(i)
            count = 0
    plaatsi = 0
    nieuw = ""
    for i in plaats:
        nieuw += corpus[plaatsi:int(i)] + replacement
        plaatsi = int(i) + len(pattern)
    nieuw += corpus[int(plaatsi):]
    print(nieuw)