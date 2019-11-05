def fibonacci_values(i):
    outlist = []

    if i == 0:
        return [0]
    elif i == 1:
        return [0, 1]

    pre_val = 0
    cur_val = 1
    nex_val = 2

    outlist = [0, 1]

    while nex_val < i:

        nex_val = pre_val + cur_val
        pre_val = cur_val
        cur_val = nex_val

        outlist.append(cur_val)

    return outlist
