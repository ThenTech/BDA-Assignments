def is_ordered(a):
    sorted = True
    for i in range(len(a) - 1):
        prev_value = a[i]
        next_value = a[i+1]
        if not prev_value <= a[i] <= next_value:
            sorted = False
            break
    return sorted
