def is_unique(l):
    new_list = []
    for i in range(0,len(l)):
        getal = l[i]
        if getal in new_list:
            return False
        if getal not in new_list:
            new_list.append(l[i])
    return True