def is_unique(l):
    unique_list = []
    for i in l:
        if i not in unique_list:
            unique_list.append(i)
    return l == unique_list