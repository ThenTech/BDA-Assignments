def shift(l, n):
    inputlist = l[:]
    shifted_list = []
    n = int(n)
    x = 0
    toobig = False

    for i in range(0, len(inputlist)):
        x = i + n
        if x >= len(inputlist):
            shift = (x % len(inputlist))
            shifted_list[shift] = inputlist[i]
        else:
            shifted_list[x] = [inputlist[i]]
    return shifted_list

print(shift([1, 2, 3, 4, 5], 2))