def shift(l, n):
    list = l[:]
    shifted_list = []
    n = int(n)
    for i in range(0, len(l)):
        x = i + n
        print(x)
        if x < len(l):
            list[i] = shifted_list[i+n]
            print(shifted_list)
        elif (x) >= len(l):
            x = x - len(l)
            list[i] = shifted_list[x]
            print(shifted_list)