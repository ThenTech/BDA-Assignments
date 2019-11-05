def shift(list, n):
    if n > 0:
        list_part = list[0:(len(list) - n)]
        list = list[len(list) - n:]
        list = list + list_part
        print(list)
        return list
    elif n < 0:
        list_part = list[0:(len(list) + n - 1)]
        list = list[len(list) + n - 1:]
        list = list + list_part
        print(list)
        return list
    else:
        return list