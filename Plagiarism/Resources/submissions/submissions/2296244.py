def shift(l, n):
    shifted_list = []
    list_len = len(l)
    
    for index, element in enumerate(l):
        shifted_list.append(l[(index + n) % (list_len - 1)])
    
    return shifted_list