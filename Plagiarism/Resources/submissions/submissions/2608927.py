def is_unique(l):
    for i in l:
        count=0
        for j in l:
            if i == j:
                count+=1
                if count > 1:
                    return False
    return True