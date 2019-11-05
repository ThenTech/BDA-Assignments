def shift(l, n):
    a = []
    for j in range(1, n):
        x = a +(l[((len(l))-n):len(l)])
    for i in range(1, n):
        x.extend(l[0:((len(l))-n)])

    print(x)







shift([1, 2, 3, 4, 5], 2)