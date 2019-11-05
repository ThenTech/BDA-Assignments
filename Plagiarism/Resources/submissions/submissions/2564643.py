
def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    l1 =[]
    for i in range(1,w1):
        l1.append(x1+i)
    print(l1)
    l2 =[]
    for i in range(1,h1):
        l2.append(y1+i)
    print(l2)
    l3 = []
    for i in range(w2+1):
        l3.append(x2 + i)
    print(l3)
    l4 = []
    for i in range(h2+1):
        l4.append(y2 + i)
    print(l4)

    for element in l1:
        print(element)
        if element in l3:

            for thing in l2:
                if thing in l4:
                    return True
                else:
                    return False
        else:
            return False