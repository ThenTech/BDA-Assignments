def shift(l, n):
    new_list = []
    for i in range(len(l)):
        new_list.append(l[i - n%len(l)])
    return new_list