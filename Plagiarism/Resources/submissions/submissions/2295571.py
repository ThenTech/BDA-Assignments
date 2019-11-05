def shift(l, n):
    shifted_list = []
    list_len = len(l)
    
    if n < 0:
        shifted_list += l[-(list_len - n):]
        shifted_list += l[:-n]
    else:
        shifted_list += l[-n:]
        shifted_list += l[:(list_len - n)]