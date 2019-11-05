def replace(pattern, replacement, corpus):
    l =[]
    m = []
    new_string = ""
    for i in range(len(corpus)-len(pattern)):
            if pattern == corpus[i:i+len(pattern)]:
                l.append(i)
    #print(l)

    for element in l:
        for number in range(1,len(pattern)):
            m.append(element + number)
    #print(m)


    for i in range(len(corpus)):
        if i in l:
            new_string += replacement
        else:
            if i not in m:
                new_string += corpus[i]
    return new_string