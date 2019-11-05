def element_x(n, list, new_list, element):
    for i in range(len(list)+1):
        if i % element != 0:
            new_list.append(list[i-1])
    return new_list
def lucky_numbers(n):
    #make list
    list = []
    for i in range(1,n+1):
        list.append(i)

    #eliminate elements
    new_list = []
    element = 1
    for i in range(n):
        element += 1
        list = element_x(n, list, [], element)
        if element > len(list):
            return list
