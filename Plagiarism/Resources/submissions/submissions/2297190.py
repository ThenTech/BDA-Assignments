def is_unique(l):
    count = []
    for x in l:
        if x in count:
            return False
        else:
            count.append(x)
    return True


print(is_unique([1, 2, 3, 4, 5, 5]))

