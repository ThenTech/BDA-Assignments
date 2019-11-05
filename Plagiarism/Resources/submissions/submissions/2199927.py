def replace(pattern, replacement, corpus):
    new_string = ""
    
    for index in range(len(corpus)):
        if corpus[index:index + len(pattern)] == pattern:
            new_string += replacement
        else:
            new_string += corpus[index]
    
    return new_string
            

