def replace(pattern, replacement, corpus):
    newword = ""
    counter = 0
    while counter < len(corpus):

        if corpus[counter:len(pattern) + counter] == pattern:
            newword += replacement
            counter += len(pattern) - 1
        else:
            newword += corpus[counter]
        counter += 1
    return newword