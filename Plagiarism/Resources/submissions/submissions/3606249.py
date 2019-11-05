def shift(l, n):
    new_list = [0 * i for i in range(len(l))]
    
    for i in range(len(l)):
        new_list[i] = l[(len(l) - n + i) % len(l)]
    return new_list
    pass