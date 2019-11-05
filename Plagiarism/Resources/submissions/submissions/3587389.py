def shift(l, n):
    shiftedList = []
    for i in l:
        shiftedList.append(0)
    
    for i in range(len(l)):
        positionAfterShift = (i + n) % len(l)
        shiftedList[positionAfterShift] = l[i]
    return shiftedList