def is_unique(l):
    for x in l:
        l.count(x)
    if l.count(x) < 2:
        return True
    else:
        return False

print(is_unique([1, 3, 3]))