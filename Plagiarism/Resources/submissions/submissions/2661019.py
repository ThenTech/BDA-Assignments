def is_unique(listy):
    for i in range(len(listy)):
        if listy[i] in listy[i+1:]:
            return False
        else:
            continue
    return True