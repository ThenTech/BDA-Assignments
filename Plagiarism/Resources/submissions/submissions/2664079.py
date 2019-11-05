def shift(list, n):
    copy = []
    for i in range(len(list)):
        # i-th element, shifted n positions
        old_i = (i - n) % len(list)
        copy.append(list[old_i])
    return copy
