f = int(input())
possible = ["A", "C", "G", "T"]
if f == 1:
    for i in possible:
        print(i)
def combinations(n):
    global f
    my_list = []
    if n == 1:
        return possible

    for j in possible:
        for i in combinations(n-1):
            h = i + j
            my_list.append(h)
    if n == f:
        for m in my_list:
            print(m)
    else:
        return(my_list)
    return
combinations(f)