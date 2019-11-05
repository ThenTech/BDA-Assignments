def is_unique(l):
    unique = True
    for i in l:
        counter = 0
        for j in l:
            if i == j:
                if counter == 0:
                    counter += 1
                else:
                    unique = False
                    break
    return unique