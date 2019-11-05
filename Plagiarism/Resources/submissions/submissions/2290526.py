def is_ordered(l):
    ordered = True
    for number in l[:len(l) - 1]:
        if l[number] <= l[number + 1]:
            ordered *= True
        else:
            ordered = False
    return ordered