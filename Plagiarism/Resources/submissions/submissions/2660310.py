def replace(pattern, replacement, corpus):
    list_locations = []
    if len(pattern) <= len(corpus):
        for i in range(len(corpus)):
            if i <= len(corpus) -1 - len(pattern):
                if pattern == corpus[i:i+len(pattern)]:
                    list_locations.append(i)

    print(list_locations)

    for i in range(len(list_locations)-1, -1, -1):
        corpus = corpus[:list_locations[i]] + replacement + corpus[list_locations[i]+len(pattern):]
    print(corpus)