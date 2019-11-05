def graph(x1, w1, x2, w2):
    
    #variables
    w1 = x1 + w1
    w2 = x2 + w2

    if x1 == x2 and w1 == w2:
        return False

    

    for i in range(x2 , w2):
        if i <= w1 and i >= x1:
            return True
    return False

def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    
    var1 = graph(x1, w1, x2, w2)
    var2 = graph(y1, h1, y2, h2)
    if var1 == True and var2 == True:
        return True
    return False