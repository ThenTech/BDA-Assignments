def is_ordered(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True


print(is_ordered([1, -2, 3, 4, 5, 6, 7, 8, 9]))