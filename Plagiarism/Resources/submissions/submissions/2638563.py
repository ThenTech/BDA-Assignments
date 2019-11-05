def count_words(string):
    inword = False
    count = 0
    for char in string:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            inword = True
        else:
            if inword:
                count += 1
            inword = False
    if inword:
        count += 1
    
    return count