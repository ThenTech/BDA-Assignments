def shift(l, n):
    shifted_list = []
    list_len = len(l)
    
    for index in enumerate(l):
        shifted_list.append( l[(index + n) % list_len] )
    
    return shifted_list