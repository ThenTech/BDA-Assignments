def replace(pattern, replacement, corpus):
    new_string = ""
    counter = 0
    
    for index in range(len(corpus)):
        if corpus[index:index + len(pattern) + 1] == pattern:
            counter = len(pattern)
            new_string += replacement
        else:
            if counter != 0:
                counter -= 1
            else:
                new_string += corpus[index]
    
    return new_string