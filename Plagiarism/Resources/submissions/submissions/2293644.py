def is_ordered(a):
    sorted = True
    prev_value = a[0]
    next_value = a[1]
    for i in range(len(a) - 1):
        if not (prev_value <= a[i] <= next_value):
            sorted = False
            break
        prev_value = a[i]
        next_value = a[i + 1]
    return sorted