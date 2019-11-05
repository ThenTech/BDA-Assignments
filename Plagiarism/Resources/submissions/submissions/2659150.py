def remove_element(list, st_index):
    index_remove_list = [(st_index + (i * (st_index + 1))) for i in range(len(list))]
    new_list = []
    for i in range(len(list)):
        if i not in index_remove_list:
            new_list.append(list[i])
    return new_list

def lucky_numbers(n):
    list = [i for i in range(1, n + 1)]
    st_index = 1
    while st_index <= len(list) - 1:
        list = remove_element(list, st_index)
        st_index += 1
        if st_index >= len(list):
            break

    return list

