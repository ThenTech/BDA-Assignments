def is_unique(l):
    New_list = []
    for i in l:
        if i not in New_list:
            New_list.append(i)
        else:
            return False
    return True