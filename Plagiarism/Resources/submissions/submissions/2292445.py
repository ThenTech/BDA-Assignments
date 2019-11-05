def is_ordered(l):
    copy = l[:]
    sorted_copy = copy.sort()

    return sorted_copy == copy

print(is_ordered([1, 5, 9, 10]))