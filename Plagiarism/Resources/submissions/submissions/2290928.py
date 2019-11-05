def is_ordered(l):
    new_list = []
    for val in l:
        new_char = val
        new_list.append(new_char)

    if new_list == l:
        return True
    else:
        return False


print(is_ordered([1, 2, 3, 4, 5, 6, 7, 8, 9]))
